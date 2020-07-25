# generate-mnist-Dataset

Some extremingly easy codes to decode the mnist dataset. To generate mnist images, first you need to download the files from http://yann.lecun.com/exdb/mnist/. Next, create two folders with names mnist_training and mnist_test. Then you can generate testing samples with commands:

```python
python genMnist.py
```
The generated testing samples will be stored in mnist_testing.

If you want to generate the training samples, please run the above command with the 7th line commented and the generated samples will be in your mnist_training folder.
