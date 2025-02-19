# Diff-Mamba
Two-stage Mamba-based Diffusion Model for Image Restoration 

<!By Lei Liu 1,2 , Luan Ma 1 , Shuai Wang 1,2,* , Jun Wang 3 and Silas N. Melo 4>



<!--

Two-stage Mamba-based Diffusion Model for Image Restoration

<img src = "https://github.com/wlydlut/Diff-Mamba/blob/main/Figs/fig1.png#pic_center">  

First Training Pipeline and Sampling Phase

<img src = "https://github.com/wlydlut/Diff-Mamba/blob/main/Figs/fig2.png#pic_center"> 

-->

Requirements

- CUDA 10.1 (or later)
- Python 3.9 (or later)
- Pytorch 1.8.1 (or later)
- Torchvision 0.19
- OpenCV 4.7.0
- tensorboard, skimage, scipy, lmdb, tqdm, yaml, einops, natsort

Training and Evaluation

Training and testing instructions for Image Deraining, Image Deblurring, and Real Image Denoising are provied in the links below. 

<table>

  <tr>

    <th align="center">Task</th>

    <th align="center">Training</th>

    <th align="center">Testing</th>

    <th align="center">Diff-Mamba's Visual Results</th>

  </tr>

   <tr>
    <td align="center">Image Deraining</td>
    <td align="center"><a href="Deraining/README.md#training">Link</a></td>
    <td align="center"><a href="Deraining/README.md#testing">Link</a></td>
    <td align="center"><a href="https://drive.google.com/drive/folders/1v4aAFDAojHtedtRmPcqVKJcAixW5dZ8m">Download</a></td>
  </tr>
  <tr>
    <td align="center">Image Deblurring</td>
    <td align="center"><a href="Deblurring/README.md#training">Link</a></td>
    <td align="center"><a href="Deblurring/README.md#testing">Link</a></td>
    <td align="center"><a href="https://drive.google.com/drive/folders/1qYVPblP0kCyfIoxDQ2NBsdbv_MoZ24S4">Download</a></td>
  </tr>
  <tr>
     <td align="center">Real Image Denoising</td>
    <td align="center"><a href="Denoising/README.md#training">Link</a></td>
    <td align="center"><a href="Denoising/README.md#testing">Link</a></td>
    <td align="center"><a href="https://drive.google.com/drive/folders/1hgSYcwSLktFh42LA9bDXTLUuNzThdJVA">Download</a></td>
  </tr>
</table>

Contact

Should you have any questions, please contact 12311080786@chnu.edu.cn 

Acknowledgment: This code is based on the BasicSR toolbox and Restormer, WeatherDiffusion. 


