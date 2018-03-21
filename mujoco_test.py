import mujoco_py

model = mujoco_py.load_model_from_path("mujoco-py/xmls/humanoid.xml")
sim = mujoco_py.MjSim(model)
viewer = mujoco_py.MjViewerBasic(sim)

print(sim.data.qpos)
i = 0
while i < 100000:
	i += 1
	sim.step()
	viewer.render()
