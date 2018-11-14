from abc import ABC, abstractmethod

class Camera(ABC):
    def __init__(self, camera_obj):
        self.camera_obj = camera_obj

    @abstractmethod
    def shoot(self):
        pass

class Photo(Camera):
    def shoot(self):
        return print('Hii!!!')

class Video(Camera):
    def shoot(self):
        return print('Yeah , that\'s great video!')

camera = Photo('Wacom')
print(camera.camera_obj)
camera.shoot()
camera2 = Video('Wacom3000')
print(camera2.camera_obj)
camera2.shoot()
