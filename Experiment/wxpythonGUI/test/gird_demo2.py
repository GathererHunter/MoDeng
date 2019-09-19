import wximport wx.gridfrom PIL import Imagefrom io import BytesIOfrom pylab import *mpl.rcParams['font.sans-serif'] = ['SimHei']matplotlib.rcParams['axes.unicode_minus'] = Falseclass MyApp(wx.App):    def OnInit(self):        frame = wx.Frame(None, -1, title="wx.Grid - Bitmap example")        grid = wx.grid.Grid(frame)        nrow, ncol = 20, 5        grid.CreateGrid(nrow, ncol)        for r in range(nrow):            for c in range(ncol-1):                fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))                plt.title('图' + str(ncol * r + c))                output = BytesIO()  # BytesIO实现了在内存中读写byte                buf_save = BytesIO()                fig.savefig(output, dpi=100)                output.seek(0)                img = wx.Image(output, wx.BITMAP_TYPE_ANY)                buf_save.close()                output.close()                imageRenderer = MyImageRenderer(wx.Bitmap(img))                grid.SetCellRenderer(r, c+1, imageRenderer)                grid.SetColSize(c+1, img.GetWidth() + 2)                grid.SetRowSize(r, img.GetHeight() + 2)        frame.Show(True)        return Trueclass MyImageRenderer(wx.grid.GridCellRenderer):    def __init__(self, img):        wx.grid.GridCellRenderer.__init__(self)        self.img = img    def Draw(self, grid, attr, dc, rect, row, col, isSelected):        image = wx.MemoryDC()        image.SelectObject(self.img)        dc.SetBackgroundMode(wx.SOLID)        if isSelected:            dc.SetBrush(wx.Brush(wx.BLUE, wx.SOLID))            dc.SetPen(wx.Pen(wx.BLUE, 1, wx.SOLID))        else:            dc.SetBrush(wx.Brush(wx.WHITE, wx.SOLID))            dc.SetPen(wx.Pen(wx.WHITE, 1, wx.SOLID))        dc.DrawRectangle(rect)        width, height = self.img.GetWidth(), self.img.GetHeight()        if width > rect.width - 2:            width = rect.width - 2        if height > rect.height - 2:            height = rect.height - 2        dc.Blit(rect.x + 1, rect.y + 1, width, height, image, 0, 0, wx.COPY, True)app = MyApp(0)app.MainLoop()