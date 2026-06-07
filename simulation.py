import time
import pybullet as p
import pybullet_data

physics_client = p.connect(p.GUI)
# p.configureDebugVisualizer(p.COV_ENABLE_GUI,0)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0, 0, -9.8)
plane_id = p.loadURDF("plane.urdf")
robot_id = p.loadURDF("body.urdf")

p.loadSDF("world.sdf")

for i in range(1000):
    p.stepSimulation()
    time.sleep(1/60)
    print(i)

p.disconnect()
