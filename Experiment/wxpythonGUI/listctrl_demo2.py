import wx
from PIL import Image
from io import BytesIO
from pylab import *

mpl.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus']=False

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(1300, 800))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('white')
        self.browserList=wx.ListCtrl(panel, size=(1200, 1200), style=wx.LC_REPORT|wx.BORDER_SUNKEN)
        self.browserList.InsertColumn(0, 'Image', width=600)
        self.browserList.InsertColumn(1, 'Browser: ', width=400)

        self.list=wx.ImageList(600, 400)
        self.browserList.SetImageList(self.list, wx.IMAGE_LIST_SMALL)



        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))
        plt.title('这是标题，看到表示有图！')
        output = BytesIO()  # BytesIO实现了在内存中读写byte
        buf_save = BytesIO()
        fig.savefig(output, dpi=100)
        output.seek(0)
        img = wx.Image(output, wx.BITMAP_TYPE_ANY)
        pic_id = wx.Bitmap(img)
        buf_save.close()
        output.close()


        fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(6, 4))
        plt.title('这是第二个图的标题！')
        output = BytesIO()  # BytesIO实现了在内存中读写byte
        buf_save = BytesIO()
        fig.savefig(output, dpi=100)
        output.seek(0)
        img = wx.Image(output, wx.BITMAP_TYPE_ANY)
        pic_id2 = wx.Bitmap(img)
        buf_save.close()
        output.close()


        # images=['./1.png','./1.png']
        # x=0
        # for i in images:
        #     img=wx.Image(i, wx.BITMAP_TYPE_ANY)
        #     img=wx.BitmapFromImage(img)
        #     browserimg=self.list.Add(img)
        # self.browserList.InsertImageItem(x, 0)
        # self.browserList.InsertImageItem(x, 1)

        browserimg = self.list.Add(pic_id)
        browserimg = self.list.Add(pic_id2)

        self.browserList.InsertItem(0, 1)
        self.browserList.InsertItem(0, 0)
        self.browserList.InsertItem(0, 1)
        self.browserList.InsertItem(0, 0)

        self.browserList.SetItem(0, 1, "Mozilla Firefox")
        self.browserList.SetItem(1, 1, "Google Chrome")
        self.browserList.SetItem(2, 1, "Mozilla Firefox")
        self.browserList.SetItem(3, 1, "Google Chrome")
#
#
# class MyFrame(wx.Frame):
#     def __init__(self, parent, id, title):
#         wx.Frame.__init__(self, parent, id, title,size=(250, 250))
#         panel = wx.Panel(self, -1)
#         panel.SetBackgroundColour('white')
#         self.browserList=wx.ListCtrl(panel, size=(1200,800),style = wx.LC_REPORT|wx.BORDER_SUNKEN)
#         self.browserList.InsertColumn(0, '', width=50)
#         self.browserList.InsertColumn(1, 'Browser: ', width=200)
#
#         self.list=wx.ImageList(400, 400)
#         self.browserList.SetImageList(self.list, wx.IMAGE_LIST_SMALL)
#         images=['mozilla.png', 'chrome.png']
#         x=0
#         for i in images:
#             img=wx.Image(i, wx.BITMAP_TYPE_ANY)
#             img=wx.BitmapFromImage(img)
#             browserimg=self.list.Add(img)
#         self.browserList.InsertImageItem(x, 0)
#         self.browserList.InsertImageItem(x, 0)
#
#         self.browserList.SetStringItem(0, 1, "Mozilla Firefox")
#         self.browserList.SetStringItem(1, 1, "Google Chrome")



class MyApp(wx.App):
     def OnInit(self):
         frame = MyFrame(None, -1, 'frame')
         frame.Show(True)
         return True

app = MyApp(0)
app.MainLoop()

end = 0