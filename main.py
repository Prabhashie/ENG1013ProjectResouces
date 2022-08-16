from EE.phase_3.project_resources.eng1013_project_resources import ENG1013ProjectResources
from project_resources import eng1013_project_resources

pr = ENG1013ProjectResources()
data = 4
srclk = 6
rclk = 7

latchSelect = {
    'SR_B1_LATCH':[7,1],
    'SR_B2_LATCH':[2,0]
}
# test values for no scrolling
val = '56'
val = [6571,3462,8093,3064]
val = [1,2,3,4,5,6,7,8,9,10]
pr.write_parallel_no_scroll(data, srclk, val, 1, latchSelect, 0.0000000001)

latchSelect = {
    'SR_B1_LATCH':[7,0],
    'SR_B2_LATCH':[2,1]
}
arr = [0,0,0,0,0,0,1,0]
pr.write_parallel_no_scroll(data, srclk, arr, 5, latchSelect, 0.0000000001)

# test values for scrolling
# val = '12.0C'
pr.write_parallel_scroll(data, srclk, val, 0.4, 8, latchSelect, 0.0000000001)