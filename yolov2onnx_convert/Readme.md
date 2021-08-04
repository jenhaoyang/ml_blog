修改https://github.com/purelyvivid/yolo2_onnx/blob/master/darknet.py 151行为

pad = int((kernel_size-1)/2) if is_pad else 0

在https://github.com/purelyvivid/yolo2_onnx/blob/master/Onnx.py中的最下方添加如下代码转化yolov2的weights和cfg文件到onnx

def onnx_file_export(model, onnxfilepath):
    """
    generate ONNX file
    used by 'save_pretrained_model_to_ONNX'
    """
    import torch.onnx
    from torch.autograd import Variable
    dummy_input = torch.randn(1, 3, 112, 112)
    torch.onnx.export(model, dummy_input, onnxfilepath)
        
from darknet import Darknet
m = Darknet(cfg_directory)
m.load_weights(weights.directory)
onnx_file_export(m,onnx_save_directory)

 
然后在cmd执行

python Onnx.py
————————————————
版权声明：本文为CSDN博主「ystsaan」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/weixin_42388228/article/details/117020439