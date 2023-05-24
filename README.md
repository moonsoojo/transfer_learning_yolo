# Transfer Learning and Computer Vision
Fine tune a pre-trained computer vision model to test the effectiveness of transfer learning.

**Domain**: medical field - colonoscopy. 27k training images, 4k validation

**Model**: YOLOv8x

In order to obtain a higher accuracy, I went a step further and performed hyperparameter variation experiments.

**Batch size**: 8, 16

**Learning rate pairs (initial, final)**: (0.001, 0.000001), (0.0001, 0.01)

**Highest accuracy obtained (mAP)**: 95.8%

**Best performing variation**: batch size of 16, learning rate pair of (0.0001, 0.01)
