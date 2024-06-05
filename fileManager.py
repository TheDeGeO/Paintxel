import colors as clr
import guiTools as gui
import tkinter as tk
import tkinter.filedialog

def saveFile(matrix: list[list[int]]):
    #Convert matrix to string
    matrixString = '\n'.join([' '.join(map(str, row)) for row in matrix])

    top = tk.Tk()
    top.withdraw()
    filename = tk.filedialog.asksaveasfilename(parent=top, title='Select file', initialdir='saves', filetypes=[('Text files', '*.txt')])
    top.destroy()

    if filename:
        with open(filename, 'w') as file:
            file.write(matrixString)
            print(f"File saved to {filename}")

        return filename
    else:
        print("No file selected")
        return None

def loadFile(pixel_size: int):
    top = tk.Tk()
    top.withdraw()
    filename = tk.filedialog.askopenfilename(parent=top, title='Select file', initialdir='saves', filetypes=[('Text files', '*.txt')])
    top.destroy()

    if filename:
        #Load numeric matrix from file
        with open(filename, 'r') as file:
            lines = file.readlines()
            numMatrix = [[int(num) for num in line.split()] for line in lines]

        #Create block matrix from numeric matrix
        matrix = []
        for i in range(len(numMatrix)):
            matrix.append([])
            for j in range(len(numMatrix[i])):
                pixel_x = j * pixel_size + pixel_size
                pixel_y = i * pixel_size + pixel_size
                num = numMatrix[i][j]
                color = clr.getNumberColor(num)
                matrix[i].append(gui.ColorBlock(color, pixel_size, pixel_x, pixel_y, 0))

        return matrix

    else:
        print("No file selected")
        return None