import pygmsh as pg
import numpy as np
from mayavi import mlab
from shapely.geometry import Polygon, LineString, CAP_STYLE, JOIN_STYLE
from matplotlib import pyplot as plt

geom1 = pg.built_in.Geometry()

pt1 = geom1.add_point( [0.5, 0, 0], lcar = 0.005)
pt2 = geom1.add_point( [1, 0, 0], lcar = 0.0025)
pt3 = geom1.add_point( [1, 0.05, 0], lcar = 0.0025)
pt4 = geom1.add_point( [0.5, 0.05, 0], lcar = 0.005)

l1 = geom1.add_line(pt1, pt2)
l2 = geom1.add_line(pt2, pt3)
l3 = geom1.add_line(pt3, pt4)
l4 = geom1.add_line(pt4, pt1)

lloop = geom1.add_line_loop([l3, l4, l1, l2])

surf = geom1.add_plane_surface(lloop)

points, cells, point_data, cell_data, field_data = pg.generate_mesh(geom1)

### Coordinates of nodes ###
x = points[:,0]
y = points[:,1]
z = points[:,2]

### Element connectivity ###
elmts_b = cells["triangle"]

### These lines are to plot the mesh ###
beam_el = mlab.pipeline.scalar_scatter(x,y,z)
delaunay = mlab.pipeline.delaunay2d(beam_el)
delaunay.filter.offset = 999    
edges = mlab.pipeline.extract_edges(delaunay)
mlab.pipeline.surface(edges, opacity=0.7, line_width=3)

#A change for second commit
# Removed shapely for some changes 
