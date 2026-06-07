import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("boxes.sdf")

height = 1
width = 1
length = 1

for z in range(10):
    for x in range(5):
        for y in range(5):
            pyrosim.Send_Cube( name=f"Box{x}{y}{z}", pos=[x, y, 0.5 + z], size=[width, length, height])

    # Update height, width, and length
    height *= 0.9
    width  *= 0.9
    length *= 0.9

pyrosim.End()
