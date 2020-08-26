import pygame

class tree:
    def __init__(self, options):
        self.options = options
        # self.length_dividor = options["length_dividor"]
        # self.thickness_dividor = options["thickness_dividor"]
        # self.semi_angle = options["semi_angle"]
        # self.thickness = options["thickness"]
        #
        # self.branches_nb = options["branches_nb"]
        #
        # self.branc_min_size = options["branc_min_size"]

        pass

    def draw(self, start_pos, win_surface):

        vec = pygame.math.Vector2((0, -self.options["trunk_length"]))
        self.draw_branch(win_surface, (start_pos[0], start_pos[1]-self.options["additional_trunk_length"]), vec, self.options["trunk_thickness"])
        pygame.draw.line(win_surface, (255, 255, 255), start_pos, (start_pos[0], start_pos[1]-self.options["additional_trunk_length"]), self.options["trunk_thickness"])
        # for i in range(10):
        #     pygame.draw.line(win_surface, (255, 255, 255), start_pos, start_pos+vec)
        #
        #     start_pos = start_pos+vec
        #
        #     vec = vec.rotate(self.semi_angle)
        #     vec.scale_to_length(vec.length()/self.size_devidor)

        # pygame.draw.line(win_surface, (255, 255, 255), (start_pos[0], start_pos[1]-win_size[1]/8), (start_pos[0]+vec.x, start_pos[1] - win_size[1] / 8 + vec.y))

    def draw_branch(self, win_surface, start_pos, vec, thickness):
        end_pos = start_pos+vec
        if int(thickness) < 1:
            thickness = 1
        pygame.draw.line(win_surface, (255, 255, 255), start_pos, end_pos, int(thickness))
        if vec.length() / self.options["length_dividor"] < self.options["branch_min_size"]:
            return
        vec.scale_to_length(vec.length() / self.options["length_dividor"])
        for i in range(self.options["branches_nb"]):
            self.draw_branch(win_surface, end_pos, vec.rotate(self.options["semi_angle"]*(i//2+1)*(-1)**i), thickness/self.options["thickness_dividor"])

        if self.options["animate_generation"]:
            pygame.display.flip()

