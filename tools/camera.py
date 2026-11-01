"""Pinhole model of the Lovers tree camera, fitted to reference_images/POV_MASTER.png.

World axes: origin on the ground directly below the lens.
  X = metres to the right of the neutral view direction
  Z = metres forward along the ground (neutral view direction)
  Y = metres up
Image: 1672 x 941 px, origin top-left.

Fit (see bible/FRAME_BIBLE.md for the working):
  horizon at y=125 px  -> pitch 14.7 deg down at f=1312 px (~65 deg horizontal FOV)
  fence posts (~1.2 m) and the hay wagon (~2.8 m with driver) both fit a lens height of ~3.6 m.
These are estimates from an AI image, not survey numbers. Change them here only, and
re-render every board when you do.
"""
import math

W, H = 1672, 941
F = 1312.0            # focal length in px
CX, CY = W / 2, 470.0
PITCH = math.radians(14.7)   # downward tilt of neutral view
CAM_H = 3.6           # lens height above ground, metres


def project(x, y, z, yaw_deg=0.0, pitch_deg=0.0):
    """World point (m) -> image (px). Returns None if behind the camera.
    yaw/pitch are the allowed head-like turns relative to neutral."""
    yaw = math.radians(yaw_deg)
    pitch = PITCH + math.radians(pitch_deg)
    # translate to camera position
    px, py, pz = x, y - CAM_H, z
    # yaw (about vertical axis)
    px, pz = px * math.cos(yaw) - pz * math.sin(yaw), px * math.sin(yaw) + pz * math.cos(yaw)
    # pitch down (about X axis)
    cy_, cz_ = py * math.cos(pitch) + pz * math.sin(pitch), -py * math.sin(pitch) + pz * math.cos(pitch)
    if cz_ <= 0.05:
        return None
    u = CX + F * px / cz_
    v = CY - F * cy_ / cz_
    return (u, v)


def ground_from_pixel(u, v):
    """Image px on the ground plane -> world (x, z). None if above horizon."""
    # ray in camera coords
    rx, ry, rz = (u - CX) / F, -(v - CY) / F, 1.0
    # undo pitch
    wy = ry * math.cos(PITCH) - rz * math.sin(PITCH)
    wz = ry * math.sin(PITCH) + rz * math.cos(PITCH)
    wx = rx
    if wy >= 0:
        return None
    t = CAM_H / -wy
    return (wx * t, wz * t)


def height_px(x, z, h):
    """Pixel height of an upright object h metres tall standing at ground (x, z)."""
    a, b = project(x, 0, z), project(x, h, z)
    return a[1] - b[1]
