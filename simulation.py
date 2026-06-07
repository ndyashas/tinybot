import time
import pybullet as p

physics_client = p.connect(p.GUI)
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)

p.loadSDF("box.sdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()
