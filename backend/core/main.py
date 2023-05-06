from canvas import Canvas
from node import Node
from shape import Shape
def main():
                    #  Y X
    my_canvas = Canvas(10,11, [(3,4)])
    # # man = manipullator()
    # # result1 = my_canvas.count_filled_cells()
    # # #print("Filled Cells" ,result1)
    # # result2 = my_canvas.count_empty_cells()
    # # #print("Empty Cells",result2)
    # # result3 = my_canvas.count_holes()
    # # #print("Hole Cells",result3)
    s1 = Shape('F')
    # s2 = Shape('N')
    # # s3 = Shape('T')
    #
    #
    # #rotate s1 with manipulator
    # #man.rotate_shape(s1,0)
    # #print cords of s1
    # #print(s1.get_coords_list())
    pos1 = (6,6)
    # pos2 = (2,2)
    # #Shape.change_cords_by_a_position(s1,pos)
    # #print(s1.get_coords_list())
    #
    print(my_canvas.check_for_out_of_bounds_when_placed_in(s1,pos1))                                    # Y X
    my_canvas.place_shape(s1,pos1)
    # my_canvas.place_shape(s2, pos2)
    print(my_canvas.get_matrix())
    # n = Node((1,2),"F")
    # print(n.get_coords())
    # n.set_coords((3,4))
    # print(n.get_coords())
    # s1 = Shape('F')
    # print(s1.get_coords_list())
    # s1.change_cords_by_a_position((1,1))
    # print(s1.get_coords_list())



main()