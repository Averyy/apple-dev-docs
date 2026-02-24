# Cropping Images Using Saliency

**Framework**: Vision

Isolate regions in an image that are most likely to draw people’s attention.

#### Overview

*Saliency* refers to what’s noticeable or important in an image. The Vision framework supports two types of saliency: *object-based* and *attention-based*.

Attention-based saliency highlights what people are likely to look at. Object-based saliency highlights foreground objects and provides a coarse segmentation of the main subjects in an image. The range of saliency is [0,1], where higher values indicate higher potential for interest or inclusion in the foreground.

Saliency has many applications:

- Automate image cropping to fit key elements.
- Generate thumbnails from an image set.
- Guide the camera to focus on a key area for blur estimation or white balance.
- Guide postprocessing by determining candidates for sharpening or lighting enhancement.
- Pan the camera to relevant shots in a photo or video album.

This article describes one application of saliency: cropping an input image to fit a given aspect ratio while keeping the most interesting element in the image. This technique works by focusing on the region most likely to draw attention at a glance.

##### Specify the Type of Saliency

Both models of saliency are based on deep-learning neural networks. The model used for object-based saliency is trained on foreground objects that have been segmented from the background. The model used for attention-based saliency is trained using eye-tracking data from human subjects looking at images.

The class of the request to generate saliency differs depending on the type of saliency you want Vision to compute:

**Swift**:

```swift
switch SaliencyType(rawValue: UserDefaults.standard.saliencyType)! {
    case .attentionBased:
        request = VNGenerateAttentionBasedSaliencyImageRequest()
    case .objectnessBased:
        request = VNGenerateObjectnessBasedSaliencyImageRequest()
}
```

**Objective-C**:

```objc
switch (saliencyType) 
{
    case kAttentionBased:
        request = [[VNGenerateAttentionBasedSaliencyImageRequest alloc] init];
        break;
    case kObjectnessBased:
        request = [[VNGenerateObjectnessBasedSaliencyImageRequest alloc] init];
        break;
}
```

Object-based saliency and attention-based saliency have different use cases. If you’re deciding what to keep in an image thumbnail based on what’s most interesting, use attention-based saliency.

##### Parse the Output Heatmap

Both types of saliency requests return their results as heatmaps, which are 68 x 68 pixel buffers of floating-point saliency values. Think of each entry in the heatmap as a cell region of your original image. The heatmap quantifies how salient the pixels in the cell are for the chosen saliency approach.

> **Note**:  Saliency is computed on individual images. While it’s possible to compute saliency on each frame of a video stream, keep in mind that the saliency of objects in the scene may vary due to subtle changes in image composition, such as image framing or new subject matter.

If your app overlays the saliency heatmap on the original input image, upsample the heatmap and apply a colormap before showing it to the user.

##### Merge Salient Regions for Object Based Saliency

For object-based saliency requests, which return up to three bounding boxes, you can use either the most salient bounding box directly to crop a region of your image, or the union of all boxes. Each bounding box comes with a score that you use to rank the relevance of regions within the image.

**Swift**:

```swift
// Create the union of all salient regions.
var unionOfSalientRegions = CGRect(x: 0, y: 0, width: 0, height: 0)
let errorPointer = NSErrorPointer(nilLiteral: ())
let salientObjects = saliencyObservation.salientObjectsAndReturnError(errorPointer)
for salientObject in salientObjects {
    unionOfSalientRegions = unionOfSalientRegions.union(salientObject.boundingBox)
}
self.salientRect = VNImageRectForNormalizedRect(unionOfSalientRegions,
                             originalImage.extent.size.width,
                             originalImage.extent.size.height)
```

**Objective-C**:

```objc
// Create the union of all salient regions.
CGRect unionOfSalientRegions = CGRectNull;
for(VNRectangleObservation* salientObject in boundingBoxes)
{
    unionOfSalientRegions = CGRectUnion(unionOfSalientRegions, salientObject.boundingBox);
}        
weakSelf.salientRect = VNImageRectForNormalizedRect(unionOfSalientRegions, 
                                                    originalImage.extent.size.width, 
                                                    originalImage.extent.size.height);
```

If the object-based saliency map value is close to zero everywhere, the image contains nothing that’s salient.

##### Crop the Image

Attention-based saliency requests return only one bounding box, which you use directly to crop the image and drop uninteresting content. Use this bounding box to find the region on which to focus:

**Swift**:

```swift
DispatchQueue.global(qos: .userInitiated).async {
    let croppedImage = originalImage.cropped(to: salientRect)
    let thumbnail =  UIImage(ciImage: croppedImage)
    DispatchQueue.main.async {
        self.imageView.image = thumbnail
    }
}
```

**Objective-C**:

```objc
dispatch_async(dispatch_get_main_queue(), ^{
    CIImage* croppedImage = [originalImage imageByCroppingToRect: self.salientRect];
    UIImage* thumbnail =  [UIImage imageWithCIImage: croppedImage];
    self.imageView.image = thumbnail;
});
```

If nothing is salient, the attention heatmap that’s returned highlights the central part of the image. This behavior reflects the fact that people tend to look at the center of an image if nothing in particular stands out to them.

##### Feed Saliency Results Into Other Vision Requests

Once you know which regions of an image are interesting, you can use the output of a saliency request as the input to another Vision request, like text recognition. The bounding boxes from saliency requests also help you localize the regions you’d like to search, so you can prioritize recognition on the most salient parts of an image, like signs or posters.

**Swift**:

```swift
let requestHandler = VNImageRequestHandler(url: imageURL, options: [:])

let request: VNRequest
switch type {
case .attentionBased:
    request = VNGenerateAttentionBasedSaliencyImageRequest()
case .objectnessBased:
    request = VNGenerateObjectnessBasedSaliencyImageRequest()
}
try? requestHandler.perform([request])
    
return request.results?.first as? VNSaliencyImageObservation
```

**Objective-C**:

```objc
NSError* error;
VNImageRequestHandler* requestHandler = [[VNImageRequestHandler alloc] initWithURL:fileURL 
                                                                       options:@{}];
[imageRequestHandler performRequests:@[request] error:&error];

return request.results.first;
```

## See Also

- [Highlighting Areas of Interest in an Image Using Saliency](highlighting-areas-of-interest-in-an-image-using-saliency.md)
  Quantify and visualize where people are likely to look in an image.
- [class VNGenerateAttentionBasedSaliencyImageRequest](vngenerateattentionbasedsaliencyimagerequest.md)
  An object that produces a heat map that identifies the parts of an image most likely to draw attention.
- [class VNGenerateObjectnessBasedSaliencyImageRequest](vngenerateobjectnessbasedsaliencyimagerequest.md)
  A request that generates a heat map that identifies the parts of an image most likely to represent objects.
- [class VNSaliencyImageObservation](vnsaliencyimageobservation.md)
  An observation that contains a grayscale heat map of important areas across an image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/cropping-images-using-saliency)*