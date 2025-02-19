# close all;clear all;
#
# denoised = load('./results/Real_Denoising/SIDD/mat/Idenoised.mat');
# gt = load('./Datasets/test/SIDD/ValidationGtBlocksSrgb.mat');
#
# denoised = denoised.Idenoised;
# gt = gt.ValidationGtBlocksSrgb;
# gt = im2single(gt);
#
# total_psnr = 0;
# total_ssim = 0;
# for i = 1:40
#     for k = 1:32
#        denoised_patch = squeeze(denoised(i,k,:,:,:));
#        gt_patch = squeeze(gt(i,k,:,:,:));
#        ssim_val = ssim(denoised_patch, gt_patch);
#        psnr_val = psnr(denoised_patch, gt_patch);
#        total_ssim = total_ssim + ssim_val;
#        total_psnr = total_psnr + psnr_val;
#    end
# end
# qm_psnr = total_psnr / (40*32);
# qm_ssim = total_ssim / (40*32);
#
# fprintf('PSNR: %f SSIM: %f\n', qm_psnr, qm_ssim);

# import scipy.io
# import numpy as np
# from skimage.metrics import structural_similarity as ssim
# from skimage.metrics import peak_signal_noise_ratio as psnr
#
# # Load .mat files
# denoised_data = scipy.io.loadmat('D:\\data\\Idenoised')
# gt_data = scipy.io.loadmat('D:\\code\\C2F-DFT-main\\Denoising\\Datasets\\test\\SIDD\\ValidationGtBlocksSrgb.mat')
#
# # Extract variables from loaded data
# denoised = denoised_data['Idenoised']
# gt = gt_data['ValidationGtBlocksSrgb']
#
# # Convert data type if needed (e.g., from uint8 to float32)
# gt = gt.astype(np.float32)
#
# total_psnr = 0
# total_ssim = 0
# # num_patches = 40 * 32
#
# # Calculate PSNR and SSIM for each patch
# for i in range(40):
#     for k in range(32):
#         denoised_patch = denoised[i, k]
#         gt_patch = gt[i, k]
#         ssim_val = ssim(denoised_patch, gt_patch, multichannel=True)
#         psnr_val = psnr(denoised_patch, gt_patch)
#         total_ssim += ssim_val
#         total_psnr += psnr_val
#
# # Calculate average PSNR and SSIM
# qm_psnr = total_psnr / (40 * 32)
# qm_ssim = total_ssim / (40 * 32)
#
# print(f'PSNR: {qm_psnr} SSIM: {qm_ssim}')

# import scipy.io
# from skimage.metrics import peak_signal_noise_ratio as psnr
# from skimage.metrics import structural_similarity as ssim
#
# # Load the .mat files
# denoised_data = scipy.io.loadmat('D:\\data\\Idenoised.mat')
# gt_data = scipy.io.loadmat('D:\\code\\C2F-DFT-main\\Denoising\\Datasets\\test\\SIDD\\ValidationGtBlocksSrgb.mat')
#
# denoised = denoised_data['Idenoised']
# gt = gt_data['ValidationGtBlocksSrgb']
#
# total_psnr = 0
# total_ssim = 0
#
# for i in range(40):
#     for k in range(32):
#         denoised_patch = denoised[i, k]
#         gt_patch = gt[i, k]
#         ssim_val = ssim(denoised_patch, gt_patch, multichannel=True)
#         psnr_val = psnr(denoised_patch, gt_patch)
#         total_ssim += ssim_val
#         total_psnr += psnr_val
#
# qm_psnr = total_psnr / (40 * 32)
# qm_ssim = total_ssim / (40 * 32)
#
# print(f'PSNR: {qm_psnr} SSIM: {qm_ssim}')



# import numpy as np
# import scipy.io as sio
# from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim
#
# # Load data
# denoised_data = sio.loadmat('D:\\data\\runmatlab\\Idenoised.mat')
# gt_data = sio.loadmat('D:\\code\\C2F-DFT-main\\Denoising\\Datasets\\test\\SIDD\\ValidationGtBlocksSrgb.mat')
#
# # Extract relevant arrays
# denoised = denoised_data['Idenoised']
# gt = gt_data['ValidationGtBlocksSrgb']
# gt = gt.astype(np.float32) / 255.0  # Convert to float and scale to [0, 1]
#
# total_psnr = 0
# total_ssim = 0
# num_images = denoised.shape[0]
# num_patches = denoised.shape[1]
#
# for i in range(num_images):
#     for k in range(num_patches):
#         denoised_patch = denoised[i, k, :, :, :]
#         gt_patch = gt[i, k, :, :, :]
#         ssim_val = ssim(denoised_patch, gt_patch, multichannel=True)
#         psnr_val = psnr(gt_patch, denoised_patch, data_range=1.0)
#         total_ssim += ssim_val
#         total_psnr += psnr_val
#
# qm_psnr = total_psnr / (num_images * num_patches)
# qm_ssim = total_ssim / (num_images * num_patches)
#
# print(f'PSNR: {qm_psnr:.6f} SSIM: {qm_ssim:.6f}')

# import numpy as np
# import scipy.io as sio
# from skimage.metrics import peak_signal_noise_ratio as psnr, structural_similarity as ssim
#
# # Load data
# denoised_data = sio.loadmat('D:\\data\\Idenoised.mat')
# gt_data = sio.loadmat('D:\\code\\C2F-DFT-main\\Denoising\\Datasets\\test\\SIDD\\ValidationGtBlocksSrgb.mat')
#
# # Extract relevant arrays
# denoised = denoised_data['Idenoised']
# gt = gt_data['ValidationGtBlocksSrgb']
# gt = gt.astype(np.float32) / 255.0  # Convert to float and scale to [0, 1]
#
# total_psnr = 0
# total_ssim = 0
# num_images = denoised.shape[0]
# num_patches = denoised.shape[1]
#
# # Function to check for NaN or infinity values in a patch
# def is_valid_patch(patch):
#     return np.all(np.isfinite(patch))
#
# for i in range(num_images):
#     for k in range(num_patches):
#         denoised_patch = denoised[i, k, :, :, :]
#         gt_patch = gt[i, k, :, :, :]
#
#         if is_valid_patch(denoised_patch) and is_valid_patch(gt_patch):
#             ssim_val = ssim(denoised_patch, gt_patch, multichannel=True)
#             psnr_val = psnr(gt_patch, denoised_patch, data_range=1.0)
#             total_ssim += ssim_val
#             total_psnr += psnr_val
#         else:
#             print(f"Invalid patch at image {i}, patch {k}. Skipping...")
#
# qm_psnr = total_psnr / (num_images * num_patches)
# qm_ssim = total_ssim / (num_images * num_patches)
#
# print(f'PSNR: {qm_psnr:.6f} SSIM: {qm_ssim:.6f}')
