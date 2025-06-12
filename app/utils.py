from PIL import Image
from torchvision import transforms
import torch 
import timm
from torch import nn


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = torch.load("/workspaces/skin-con/model/skin_model.pth",map_location=device, weights_only=False)

softmax = nn.Softmax(dim=1)

# set up the transformation 

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.RandomHorizontalFlip(p=0.3),
    transforms.ColorJitter(brightness=0.1, contrast=0.0, saturation=0.0, hue= 0.0),
    transforms.RandomRotation(15),
    transforms.Resize((224,224)),
    transforms.Normalize([0.485, 0.456, 0.406],[0.229, 0.224, 0.225])
    ])


# Ensure skin_con is a list
skin_con = ['Boil','clear skin','Eczema','keloids','Vitiligo']

def predict_image(image_path):
    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0).to(device)

    with torch.no_grad():
        outputs = model(image)
        outputs = softmax(outputs)
        probs, preds = torch.max(outputs, 1)
        probs, preds = probs.item(), preds.item()

    return probs, skin_con[preds]

# Run
if __name__ == "__main__":
    image_path = input("Enter image path: ")
    print(predict_image(image_path))
