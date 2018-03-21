import gym
from gym.envs.mujoco import humanoid

env = humanoid.HumanoidEnv()
while True:
	env.step(env.action_space.sample())
	env.render()