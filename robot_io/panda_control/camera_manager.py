import cv2
import hydra


class CameraManager:
    """
    Class for handling different cameras
    """
    def __init__(self, use_gripper_cam, use_static_cam, gripper_cam, static_cam):
        self.gripper_cam = None
        self.static_cam = None
        if use_gripper_cam:
            self.gripper_cam = hydra.utils.instantiate(gripper_cam)
        if use_static_cam:
            self.static_cam = hydra.utils.instantiate(static_cam)
        self.obs = None

    def get_images(self):
        obs = {}
        if self.gripper_cam is not None:
            rgb_gripper, depth_gripper = self.gripper_cam.get_image()
            obs['rgb_gripper'] = rgb_gripper
            obs['depth_gripper'] = depth_gripper
        if self.static_cam is not None:
            rgb, depth = self.static_cam.get_image()
            obs[f'rgb_static'] = rgb
            obs[f'depth_static'] = depth
        self.obs = obs
        return obs

    def render(self):
        if "rgb_gripper" in self.obs:
            cv2.imshow("rgb_gripper", self.obs["rgb_gripper"][:, :, ::-1])
        if "rgb_static" in self.obs:
            cv2.imshow("rgb_static", self.obs["rgb_static"][:, :, ::-1])
        cv2.waitKey(1)
