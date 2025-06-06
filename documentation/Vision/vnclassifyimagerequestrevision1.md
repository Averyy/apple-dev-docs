# VNClassifyImageRequestRevision1

**Framework**: Vision  
**Kind**: var

A constant for specifying the first revision of the image-classification request.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
let VNClassifyImageRequestRevision1: Int
```

#### Discussion

The revision number is a constant that you pass on a per-request basis to indicate to the Vision framework which version of the image classifier to use for that request. Each OS release in which the framework improves aspects of the algorithm (recognition speed, accuracy, number of languages supported, and so forth), the revision number increments by 1.

By default, recognition requests use the latest—the highest—revision number for the SDK that your app links against. If you don’t recompile your app against a newer SDK, your app binary uses the revision that was the default at the time you last compiled it. If you do recompile, your app uses the default of the new SDK.

If your app must support users on older OS versions that don’t have access to the latest Vision framework, you may want to specify an earlier revision. For example, your algorithm may depend on specific behavior from a Vision request, such as writing your image processing algorithm to assume the size or aspect ratio of bounding boxes from an older revision of the face detector. In such a scenario, you can support earlier versions of the algorithm by specifying lower numbers:

## See Also

- [var VNVisionVersionNumber: Double](vnvisionversionnumber.md)
  The current version number of the Vision framework.
- [let VNDetectAnimalBodyPoseRequestRevision1: Int](vndetectanimalbodyposerequestrevision1.md)
  A value that indicates the first revision for an animal body-pose request.
- [let VNDetectHumanBodyPose3DRequestRevision1: Int](vndetecthumanbodypose3drequestrevision1.md)
  A value that indicates the first revision for a human 3D body pose request.
- [let VNTrackHomographicImageRegistrationRequestRevision1: Int](vntrackhomographicimageregistrationrequestrevision1.md)
  A value that indicates the first revision for a homographic image-registration request.
- [let VNTrackTranslationalImageRegistrationRequestRevision1: Int](vntracktranslationalimageregistrationrequestrevision1.md)
  A value that indicates the first revision for a translational image-registration request.
- [let VNTrackOpticalFlowRequestRevision1: Int](vntrackopticalflowrequestrevision1.md)
  A value that indicates the first revision for an optial-flow request.
- [let VNClassifyImageRequestRevision2: Int](vnclassifyimagerequestrevision2.md)
  A value that indicates the second revision for an image-classification request.
- [let VNGenerateObjectnessBasedSaliencyImageRequestRevision2: Int](vngenerateobjectnessbasedsaliencyimagerequestrevision2.md)
  A value that indicates the second revision for an image-classification request.
- [let VNGenerateAttentionBasedSaliencyImageRequestRevision2: Int](vngenerateattentionbasedsaliencyimagerequestrevision2.md)
  A value that indicates the second revision for an attention-saliency image request.
- [let VNGenerateImageFeaturePrintRequestRevision1: Int](vngenerateimagefeatureprintrequestrevision1.md)
  A constant for specifying the first revision of the feature-print request.
- [let VNGenerateImageFeaturePrintRequestRevision2: Int](vngenerateimagefeatureprintrequestrevision2.md)
  A value that indicates the second revision for a feature-print request.
- [let VNDetectFaceCaptureQualityRequestRevision3: Int](vndetectfacecapturequalityrequestrevision3.md)
  A value that indicates the third revision for a face capture-quality request.
- [let VNDetectBarcodesRequestRevision4: Int](vndetectbarcodesrequestrevision4.md)
  A value that indicates the fourth revision for a barcode request.
- [let VNCalculateImageAestheticsScoresRequestRevision1: Int](vncalculateimageaestheticsscoresrequestrevision1.md)
  A value that indicates the first revision for an aesthetics scores request.
- [let VNRequestRevisionUnspecified: Int](vnrequestrevisionunspecified.md)
  A constant for specifying an unspecified request revision.


---

*[View on Apple Developer](https://developer.apple.com/documentation/vision/vnclassifyimagerequestrevision1)*