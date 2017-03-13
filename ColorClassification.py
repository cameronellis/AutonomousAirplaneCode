# This code is NOT mine. I only modified it in order to integrate it into the team's software package
import webcolors

#3 random RGB values from 0-255
#
rand1 = 200
rand2 = 200
rand3 = 200

requested_colour = [rand1, rand2, rand3]

def closest_colour(requested_colour):
	min_colours = {}
   	#key - starting variable
	for key, name in webcolors.css3_hex_to_names.items():
    	r_c, g_c, b_c = webcolors.hex_to_rgb(key)
    	rd = (r_c - requested_colour[0]) ** 2
    	gd = (g_c - requested_colour[1]) ** 2
    	bd = (b_c - requested_colour[2]) ** 2
    	min_colours[(rd + gd + bd)] = name
	temp = sorted(min_colours.items(), key=lambda s: s[0])
	return min_colours[min(min_colours.keys())]

def get_colour_name(requested_colour):
	try:
    	closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
	except ValueError:
    	closest_name = closest_colour(requested_colour)
	return closest_name

closest_name = get_colour_name(requested_colour)

print closest_name
