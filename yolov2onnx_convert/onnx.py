import os
import subprocess
import time


def make_dir(new_folder_name=""):
    """
    create sub-folder under current folder  
    """
    if not os.path.isdir(os.getcwd()+'/'+new_folder_name):
        subprocess.call("mkdir {}".format(new_folder_name), shell=True)
        print ("New Folder [{}]".format(new_folder_name))
    else:
        print ("Folder [{}] has already exist!".format(new_folder_name))
        
def prepare_backend(model, framework="tensorflow", device="CUDA:0"): 
    """
    prepare backend for Inference  
    framework = "tensorflow" or "caffe2"
    device = "CUDA:0" or "CPU" 
    """
    print('Prepare_backend with [{}] using [{}]...start'.format(framework,device));st = time.time()
    if framework == "tensorflow": 
        import onnx_tf.backend as backend
        rep = backend.prepare(model, device=device)   
    elif framework == "caffe2": 
        import onnx_caffe2.backend as backend
        rep = backend.prepare(model, device=device) 
    print('Prepare_backend [{}] [{}]...done, {:.2f} sec'.format(framework,device,time.time()-st))
    return rep, backend

class OnnxImportExport(): 

    w_img = 416
    h_img = 416   # YOLO,  3 channels, 416*416,; ImageNet, 3 channels, 224*224,
    is_obj_det = True # Object Detect or Image Classification
    
    def __init__(self, ):
        make_dir("onnx")
            
    def onnx_file_export(self, model, onnxfilepath):
        """
        generate ONNX file
        used by 'save_pretrained_model_to_ONNX'
        """
        if os.path.isfile(os.getcwd()+onnxfilepath[1:]):
            print('Onnx file has already exist!')
            return
        else:
            import torch.onnx
            from torch.autograd import Variable
            dummy_input = Variable(torch.randn(1, 3, self.w_img, self.h_img))
            print('Onnx file export [{}]...start'.format(onnxfilepath));st = time.time()
            torch.onnx.export(model, dummy_input, onnxfilepath )
            print('Onnx file export [{}]... done, {:.2f} sec'.format(onnxfilepath,time.time()-st))
        
    def save_pretrained_model_to_ONNX(self,modelName="yolo2"):
        """
        load pretrained_model,
        save to ONNX (generate .onnx)
        """
        onnxfilepath = "./onnx/{}.onnx".format(modelName)
        if modelName == "yolo2":
            self.is_obj_det = True
            self.w_img, self.h_img = 416, 416
            cfgfile =  './cfg/yolo.cfg' 
            weightfile =  './yolo.weights'
            # ref: 1.yolo2_pytorch_onnx_save_model.ipynb
            #---chk cfgfile---
            if not os.path.isfile(os.getcwd()+cfgfile[1:]) : print('cfg file Error!')
            #---download weight---
            if not os.path.isfile(os.getcwd()+weightfile[1:]) :
                st = time.time()
                print('Downloading weights [{}] from Web... start'.format(weightfile));st = time.time()
                subprocess.call("wget http://pjreddie.com/media/files/yolo.weights", shell=True)
                print('Downloading weights [{}] from Web... done, {:.2f} sec'.format(weightfile,time.time()-st))
            else:
                print('Weights file [{}] has already exist!'.format(weightfile))
            #---get model---
            from darknet import Darknet
            m = Darknet(cfgfile) 
            print('Loading weights from local [{}]... start'.format(weightfile));st = time.time()
            m.load_weights(weightfile)
            print('Loading weights from local [{}]... done, {:.2f} sec'.format(weightfile,time.time()-st))
            #---save detection information---
            import pickle
            op_dict = {
                'num_classes':m.num_classes,
                'anchors':m.anchors,
                'num_anchors':m.num_anchors
            }
            pklfilepath = '{}_detection_information.pkl'.format(modelName)
            pickle.dump(op_dict, open(pklfilepath,'wb'))
            print('Dump pickle file of detection_information [{}]...done'.format(pklfilepath))
            #---use Onnx to convert model---
            self.onnx_file_export(m, onnxfilepath)
        else: 
            self.is_obj_det = False
            self.w_img, self.h_img = 224, 224
            #---get model---
            # ref: 3.vggnet_onnx.ipynb 
            import torchvision
            if hasattr(torchvision.models, modelName):
                m = getattr(torchvision.models, modelName)(pretrained=True)
                self.onnx_file_export(m, onnxfilepath)
            else:
                print( "Wrong model name: [{}]".format(modelName))
        return self.is_obj_det, self.w_img, self.h_img

    def load_model_from_ONNX(self,modelName="yolo2"):
        """
        import (.onnx) file
        build model (model contains weights and structure)
        """
        import onnx
        # Load the ONNX model
        onnxfilepath = "./onnx/{}.onnx".format(modelName)
        if os.path.isfile(os.getcwd()+onnxfilepath[1:]) :
            print('Load onnx file [{}]...start'.format(onnxfilepath));st = time.time()
            model = onnx.load(onnxfilepath)
            print('Load onnx file [{}]...done, {:.2f} sec'.format(onnxfilepath,time.time()-st))
            # Check that the IR is well formed
            onnx.checker.check_model(model)
            # Print a human readable representation of the graph
            model_flat_IR = onnx.helper.printable_graph(model.graph)
            return model, model_flat_IR
        else:
            print('Onnx file path Error!')


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