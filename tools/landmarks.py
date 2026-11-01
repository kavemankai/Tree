"""Locked landmark geometry traced from reference_images/POV_MASTER.png (1672x941 px).
Every seasonal plate and every board panel must match these within ~6 px.
"""
HORIZON_Y = 125

# fence: top rail polyline and (x, top_y, bottom_y) for each visible post
FENCE_TOP_RAIL = [(0, 335), (245, 312), (445, 292), (595, 277), (720, 266),
                  (820, 257), (912, 247), (1040, 237), (1130, 230), (1340, 213)]
FENCE_POSTS = [(15, 330, 430), (245, 310, 400), (445, 290, 370), (595, 275, 345),
               (720, 265, 325), (820, 255, 305), (912, 245, 292), (985, 240, 285),
               (1040, 235, 278), (1090, 232, 270), (1130, 230, 265)]

# road edges, left to right, ending at the bend behind the wagon
ROAD_NEAR_EDGE = [(0, 690), (200, 650), (400, 600), (600, 545), (800, 470),
                  (1100, 380), (1350, 320), (1500, 255)]
ROAD_FAR_EDGE = [(0, 455), (200, 428), (400, 400), (600, 375), (800, 345),
                 (1000, 320), (1150, 298), (1300, 255), (1360, 218)]

PUDDLES = {
    'big_left': (230, 460, 730, 630),
    'mid': (540, 400, 645, 428),
    'right': (1030, 342, 1150, 388),
}
CASTLE_BOX = (800, 90, 925, 126)
SUN_XY = (395, 80)

# ground-plane stage zones: name -> (x_min, x_max, z_min, z_max, rgb), metres
ZONES = {
    'STAGE A (meetings)': (-2.5, 3.5, 5.6, 8.5, (120, 255, 140)),
    'STAGE B (road verge)': (-2.0, 1.5, 9.0, 10.5, (255, 230, 120)),
    'ENTRY R': (5.0, 9.0, 7.0, 12.0, (255, 140, 220)),
}
