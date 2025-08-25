import geopandas as gpd
from shapely.geometry import Point
from shapely.geometry import LineString
from shapely.geometry import Polygon
from shapely.geometry import LinearRing
from shapely.geometry import MultiPoint, MultiLineString, MultiPolygon
from shapely.geometry import box

import matplotlib.pyplot as plt

point1 = Point(2.2, 4.2)
point2 = Point(7.2, -25.1)
point3 = Point(9.26, -2.456)
point4_3D = Point(9.26, -2.456, 0.57)
gdf = gpd.GeoDataFrame(geometry=[point1])
gdf1 = gpd.GeoDataFrame(geometry=[point2])
gdf2 = gpd.GeoDataFrame(geometry=[point3])
gdf3 = gpd.GeoDataFrame(geometry=[point4_3D])


# gdf.plot()
# plt.show()

print(point1)
print(point4_3D)

print(type(point1))
print(point1.geom_type)
print(list(point1.coords))

x = point1.x
y = point1.y

print(x, y)

x = point4_3D.x
y = point4_3D.y
z = point4_3D.z

print(x, y, z)

print(point1)
print(point2)

# Calculate the distance between point1 and point2
dist = point1.distance(point2)

# Print out a nicely formatted info message
print(f"Distance between the points is {dist:.2f} units")

# Create a LineString from our Point objects

print("LINE")
line = LineString([point1, point2, point3])
line2 = LineString([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
print(line == line2)

line_plot = gpd.GeoDataFrame(geometry=[line])

# line_plot.plot()
# plt.show()

print(type(line))

print(list(line.coords))

xcoords = list(line.xy[0])
ycoords = list(line.xy[1])

print(xcoords)
print(ycoords)

print(line.length)
print(line.centroid)

print("POLYGON")
polygon1 = Polygon([(2.2, 4.2), (7.2, -25.1), (9.26, -2.456)])
polygon2 = Polygon([point1, point2, point3])

shell = LinearRing([point1, point2, point3, point1])
polygon3 = Polygon(shell)

polygon_plot = gpd.GeoDataFrame(geometry=[polygon1])
# polygon_plot.plot()
# plt.show()

print(polygon1 == polygon2 == polygon3)
print(polygon1)

print("Polygons with holes")

outer = LinearRing([(-180, 90), (-180, -90), (180, -90), (180, 90)])
hole = LinearRing([(-170, 80), (-100, -80), (100, -80), (170, 80)])

outer_plot = gpd.GeoDataFrame(geometry=[outer])
inner_plot = gpd.GeoDataFrame(geometry=[hole])

# outer_plot.plot()
# inner_plot.plot()
# plt.show()

polygon_without_hole = Polygon(outer)
polygon_with_hole = Polygon(outer, [hole])
ply_no_hole = gpd.GeoDataFrame(geometry=[polygon_without_hole])
ply_hole = gpd.GeoDataFrame(geometry=[polygon_with_hole])
# ply_hole.plot()
# plt.show()

print(polygon_without_hole)
print(polygon_with_hole)

print(f"Polygon centroid: {polygon_with_hole.centroid}")
print(f"Polygon area: {polygon_with_hole.area}")
print(f"Polygon bounding box: {polygon_with_hole.bounds}")
print(f"Polygon exterior ring: {polygon_with_hole.exterior}")
print(f"Polygon circumference: {polygon_with_hole.exterior.length}")

point = Point((0, 0))
point = point.buffer(100)

circle = gpd.GeoDataFrame(geometry=[point])
# circle.plot()
# plt.show()


# Create a MultiPoint object of our points 1,2 and 3
multipoint = MultiPoint([point1, point2, point3])

# We can also create a MultiLineString with two lines
line1 = LineString([point1, point2])
line2 = LineString([point2, point3])
multiline = MultiLineString([line1, line2])
multipoint = multipoint.envelope
multipoint_plt = gpd.GeoDataFrame(geometry=[multipoint])
multiline_plt = gpd.GeoDataFrame(geometry=[multiline])
multipoint_plt.plot()
plt.show()


# multiline_plt.plot()
# plt.show()
print(multipoint)
print(multiline)

min_x = 0
max_x = 180
min_y = -90
max_y = 90

western_hemisphere = Polygon([(-180, 90), (-180, -90), (0, -90), (0, 90)])
eastern_hemisphere = box(min_x, min_y, max_x, max_y)

eastern_hemisphere_plt = gpd.GeoDataFrame(geometry=[eastern_hemisphere])
# eastern_hemisphere_plt.plot()
# plt.show()

multipolygon = MultiPolygon([western_hemisphere, eastern_hemisphere])
multipolygon_plt = gpd.GeoDataFrame(geometry=[multipolygon])
# multipolygon_plt.plot()


# plt.show()
