from PIL import Image
base = Image.open("base.jpg")   
depth = Image.open("depth.png")   # darker colors in depth map mean the item in frame is further away from the camera. Closer items are lighter colored.
normal = Image.open("normal.png")
"""Normal maps: 
    So map as a whole will be colored 235, 84, 255
    
    Whiter colored items are supposed to be outward bumps
    Blacker colored items are supposed to be inward bumps. 

"""
out = Image.new('RGB', base.size, 0xffffff)

rL1=int(input("give light color r: "))
gL1 = int(input("give light color g: "))
bL1 = int(input("give light color b: "))
intesity = float(input("from 0-10 how strong should the shading appear?: (for a reasonable result, input a number from 0-1 )")) 
lightColor = (rL1, gL1, bL1)

print(f"Light RGB color is: r: {rL1}, g: {gL1}, b: {bL1}")

width, height = base.size
for x in range(width):
    for y in range(height):
        r,g,b = base.getpixel((x,y))
        r1,g1,b1 = depth.getpixel((x,y))
        r2, g2, b2 = normal.getpixel((x,y))
        total = r1+b1+g1
        i = intesity
        totalN = r2 + g2 + b2

        if(total != 0):
            total += 1
            if(r2 == 235 and g2 == 84 and b2 == 255):
                
                newR = int((((765/total)*(0.3*(i))) * rL1) + r)
                newG = int((((765/total)*(0.3 * i)) * gL1) + g)
                newB = int((((765/total)*(0.3 * i)) * bL1) + b)
            else:
                
                newR = int((((765/total)*(0.3*(i * (totalN/765)))) * rL1) + r)
                newG = int((((765/total)*(0.3 * i* (totalN/765))) * gL1) + g)
                newB = int((((765/total)*(0.3 * i* (totalN/765))) * bL1) + b)
        elif total <= 3:
            newR = int((((0.2*(i))) * rL1) + r)
            newG = int((((0.2 * i)) * gL1) + g)
            newB = int((((0.2 * i)) * bL1) + b)

        newColor = (newR, newG, newB)


        
        out.putpixel((x,y), (newR, newG, newB))

out.save('out.png')