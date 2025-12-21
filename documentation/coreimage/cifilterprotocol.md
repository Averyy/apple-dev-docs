# CIFilterProtocol

**Framework**: Core Image  
**Kind**: protocol

The properties you use to configure a Core Image filter.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CIFilterProtocol
```

## Topics

### Instance Properties
- [var outputImage: CIImage?](cifilterprotocol/outputimage.md)
  A [`CIImage`](ciimage.md) object that encapsulates the operations configured in the filter.
### Type Methods
- [static func customAttributes() -> [String : Any]?](cifilterprotocol/customattributes.md)
  Returns a dictionary that contains key-value pairs that describe the filter.

## Relationships

### Inherited By
- [CIAccordionFoldTransition](ciaccordionfoldtransition.md)
- [CIAffineClamp](ciaffineclamp.md)
- [CIAffineTile](ciaffinetile.md)
- [CIAreaAverage](ciareaaverage.md)
- [CIAreaAverageMaximumRed](ciareaaveragemaximumred.md)
- [CIAreaBoundsRed](ciareaboundsred.md)
- [CIAreaHistogram](ciareahistogram.md)
- [CIAreaLogarithmicHistogram](ciarealogarithmichistogram.md)
- [CIAreaMaximum](ciareamaximum.md)
- [CIAreaMaximumAlpha](ciareamaximumalpha.md)
- [CIAreaMinMax](ciareaminmax.md)
- [CIAreaMinMaxRed](ciareaminmaxred.md)
- [CIAreaMinimum](ciareaminimum.md)
- [CIAreaMinimumAlpha](ciareaminimumalpha.md)
- [CIAreaReductionFilter](ciareareductionfilter.md)
- [CIAttributedTextImageGenerator](ciattributedtextimagegenerator.md)
- [CIAztecCodeGenerator](ciazteccodegenerator.md)
- [CIBarcodeGenerator](cibarcodegenerator.md)
- [CIBarsSwipeTransition](cibarsswipetransition.md)
- [CIBicubicScaleTransform](cibicubicscaletransform.md)
- [CIBlendWithMask](ciblendwithmask.md)
- [CIBloom](cibloom.md)
- [CIBlurredRectangleGenerator](ciblurredrectanglegenerator.md)
- [CIBlurredRoundedRectangleGenerator](ciblurredroundedrectanglegenerator.md)
- [CIBokehBlur](cibokehblur.md)
- [CIBoxBlur](ciboxblur.md)
- [CIBumpDistortion](cibumpdistortion.md)
- [CIBumpDistortionLinear](cibumpdistortionlinear.md)
- [CICMYKHalftone](cicmykhalftone.md)
- [CICannyEdgeDetector](cicannyedgedetector.md)
- [CICheckerboardGenerator](cicheckerboardgenerator.md)
- [CICircleSplashDistortion](cicirclesplashdistortion.md)
- [CICircularScreen](cicircularscreen.md)
- [CICircularWrap](cicircularwrap.md)
- [CICode128BarcodeGenerator](cicode128barcodegenerator.md)
- [CIColorAbsoluteDifference](cicolorabsolutedifference.md)
- [CIColorClamp](cicolorclamp.md)
- [CIColorControls](cicolorcontrols.md)
- [CIColorCrossPolynomial](cicolorcrosspolynomial.md)
- [CIColorCube](cicolorcube.md)
- [CIColorCubeWithColorSpace](cicolorcubewithcolorspace.md)
- [CIColorCubesMixedWithMask](cicolorcubesmixedwithmask.md)
- [CIColorCurves](cicolorcurves.md)
- [CIColorInvert](cicolorinvert.md)
- [CIColorMap](cicolormap.md)
- [CIColorMatrix](cicolormatrix.md)
- [CIColorMonochrome](cicolormonochrome.md)
- [CIColorPolynomial](cicolorpolynomial.md)
- [CIColorPosterize](cicolorposterize.md)
- [CIColorThreshold](cicolorthreshold.md)
- [CIColorThresholdOtsu](cicolorthresholdotsu.md)
- [CIColumnAverage](cicolumnaverage.md)
- [CIComicEffect](cicomiceffect.md)
- [CICompositeOperation](cicompositeoperation.md)
- [CIConvertLab](ciconvertlab.md)
- [CIConvolution](ciconvolution.md)
- [CICopyMachineTransition](cicopymachinetransition.md)
- [CICoreMLModel](cicoremlmodel.md)
- [CICrystallize](cicrystallize.md)
- [CIDepthOfField](cidepthoffield.md)
- [CIDepthToDisparity](cidepthtodisparity.md)
- [CIDiscBlur](cidiscblur.md)
- [CIDisintegrateWithMaskTransition](cidisintegratewithmasktransition.md)
- [CIDisparityToDepth](cidisparitytodepth.md)
- [CIDisplacementDistortion](cidisplacementdistortion.md)
- [CIDissolveTransition](cidissolvetransition.md)
- [CIDistanceGradientFromRedMask](cidistancegradientfromredmask.md)
- [CIDither](cidither.md)
- [CIDocumentEnhancer](cidocumentenhancer.md)
- [CIDotScreen](cidotscreen.md)
- [CIDroste](cidroste.md)
- [CIEdgePreserveUpsample](ciedgepreserveupsample.md)
- [CIEdgeWork](ciedgework.md)
- [CIEdges](ciedges.md)
- [CIEightfoldReflectedTile](cieightfoldreflectedtile.md)
- [CIExposureAdjust](ciexposureadjust.md)
- [CIFalseColor](cifalsecolor.md)
- [CIFlashTransition](ciflashtransition.md)
- [CIFourCoordinateGeometryFilter](cifourcoordinategeometryfilter.md)
- [CIFourfoldReflectedTile](cifourfoldreflectedtile.md)
- [CIFourfoldRotatedTile](cifourfoldrotatedtile.md)
- [CIFourfoldTranslatedTile](cifourfoldtranslatedtile.md)
- [CIGaborGradients](cigaborgradients.md)
- [CIGammaAdjust](cigammaadjust.md)
- [CIGaussianBlur](cigaussianblur.md)
- [CIGaussianGradient](cigaussiangradient.md)
- [CIGlassDistortion](ciglassdistortion.md)
- [CIGlassLozenge](ciglasslozenge.md)
- [CIGlideReflectedTile](ciglidereflectedtile.md)
- [CIGloom](cigloom.md)
- [CIHatchedScreen](cihatchedscreen.md)
- [CIHeightFieldFromMask](ciheightfieldfrommask.md)
- [CIHexagonalPixellate](cihexagonalpixellate.md)
- [CIHighlightShadowAdjust](cihighlightshadowadjust.md)
- [CIHistogramDisplay](cihistogramdisplay.md)
- [CIHoleDistortion](ciholedistortion.md)
- [CIHueAdjust](cihueadjust.md)
- [CIHueSaturationValueGradient](cihuesaturationvaluegradient.md)
- [CIKMeans](cikmeans.md)
- [CIKaleidoscope](cikaleidoscope.md)
- [CIKeystoneCorrectionCombined](cikeystonecorrectioncombined.md)
- [CIKeystoneCorrectionHorizontal](cikeystonecorrectionhorizontal.md)
- [CIKeystoneCorrectionVertical](cikeystonecorrectionvertical.md)
- [CILabDeltaE](cilabdeltae.md)
- [CILanczosScaleTransform](cilanczosscaletransform.md)
- [CILenticularHaloGenerator](cilenticularhalogenerator.md)
- [CILightTunnel](cilighttunnel.md)
- [CILineOverlay](cilineoverlay.md)
- [CILineScreen](cilinescreen.md)
- [CILinearGradient](cilineargradient.md)
- [CILinearToSRGBToneCurve](cilineartosrgbtonecurve.md)
- [CIMaskToAlpha](cimasktoalpha.md)
- [CIMaskedVariableBlur](cimaskedvariableblur.md)
- [CIMaximumComponent](cimaximumcomponent.md)
- [CIMaximumScaleTransform](cimaximumscaletransform.md)
- [CIMedian](cimedian.md)
- [CIMeshGenerator](cimeshgenerator.md)
- [CIMinimumComponent](ciminimumcomponent.md)
- [CIMix](cimix.md)
- [CIModTransition](cimodtransition.md)
- [CIMorphologyGradient](cimorphologygradient.md)
- [CIMorphologyMaximum](cimorphologymaximum.md)
- [CIMorphologyMinimum](cimorphologyminimum.md)
- [CIMorphologyRectangleMaximum](cimorphologyrectanglemaximum.md)
- [CIMorphologyRectangleMinimum](cimorphologyrectangleminimum.md)
- [CIMotionBlur](cimotionblur.md)
- [CINinePartStretched](cininepartstretched.md)
- [CINinePartTiled](cinineparttiled.md)
- [CINoiseReduction](cinoisereduction.md)
- [CIOpTile](cioptile.md)
- [CIPDF417BarcodeGenerator](cipdf417barcodegenerator.md)
- [CIPageCurlTransition](cipagecurltransition.md)
- [CIPageCurlWithShadowTransition](cipagecurlwithshadowtransition.md)
- [CIPaletteCentroid](cipalettecentroid.md)
- [CIPalettize](cipalettize.md)
- [CIParallelogramTile](ciparallelogramtile.md)
- [CIPersonSegmentation](cipersonsegmentation.md)
- [CIPerspectiveCorrection](ciperspectivecorrection.md)
- [CIPerspectiveRotate](ciperspectiverotate.md)
- [CIPerspectiveTile](ciperspectivetile.md)
- [CIPerspectiveTransform](ciperspectivetransform.md)
- [CIPerspectiveTransformWithExtent](ciperspectivetransformwithextent.md)
- [CIPhotoEffect](ciphotoeffect.md)
- [CIPinchDistortion](cipinchdistortion.md)
- [CIPixellate](cipixellate.md)
- [CIPointillize](cipointillize.md)
- [CIQRCodeGenerator](ciqrcodegenerator.md)
- [CIRadialGradient](ciradialgradient.md)
- [CIRandomGenerator](cirandomgenerator.md)
- [CIRippleTransition](cirippletransition.md)
- [CIRoundedQRCodeGenerator](ciroundedqrcodegenerator.md)
- [CIRoundedRectangleGenerator](ciroundedrectanglegenerator.md)
- [CIRoundedRectangleStrokeGenerator](ciroundedrectanglestrokegenerator.md)
- [CIRowAverage](cirowaverage.md)
- [CISRGBToneCurveToLinear](cisrgbtonecurvetolinear.md)
- [CISaliencyMap](cisaliencymap.md)
- [CISepiaTone](cisepiatone.md)
- [CIShadedMaterial](cishadedmaterial.md)
- [CISharpenLuminance](cisharpenluminance.md)
- [CISignedDistanceGradientFromRedMask](cisigneddistancegradientfromredmask.md)
- [CISixfoldReflectedTile](cisixfoldreflectedtile.md)
- [CISixfoldRotatedTile](cisixfoldrotatedtile.md)
- [CISmoothLinearGradient](cismoothlineargradient.md)
- [CISobelGradients](cisobelgradients.md)
- [CISpotColor](cispotcolor.md)
- [CISpotLight](cispotlight.md)
- [CIStarShineGenerator](cistarshinegenerator.md)
- [CIStraighten](cistraighten.md)
- [CIStretchCrop](cistretchcrop.md)
- [CIStripesGenerator](cistripesgenerator.md)
- [CISunbeamsGenerator](cisunbeamsgenerator.md)
- [CISwipeTransition](ciswipetransition.md)
- [CISystemToneMap](cisystemtonemap.md)
- [CITemperatureAndTint](citemperatureandtint.md)
- [CITextImageGenerator](citextimagegenerator.md)
- [CIThermal](cithermal.md)
- [CIToneCurve](citonecurve.md)
- [CIToneMapHeadroom](citonemapheadroom.md)
- [CITorusLensDistortion](citoruslensdistortion.md)
- [CITransitionFilter](citransitionfilter.md)
- [CITriangleKaleidoscope](citrianglekaleidoscope.md)
- [CITriangleTile](citriangletile.md)
- [CITwelvefoldReflectedTile](citwelvefoldreflectedtile.md)
- [CITwirlDistortion](citwirldistortion.md)
- [CIUnsharpMask](ciunsharpmask.md)
- [CIVibrance](civibrance.md)
- [CIVignette](civignette.md)
- [CIVignetteEffect](civignetteeffect.md)
- [CIVortexDistortion](civortexdistortion.md)
- [CIWhitePointAdjust](ciwhitepointadjust.md)
- [CIXRay](cixray.md)
- [CIZoomBlur](cizoomblur.md)

## See Also

- [Blur Filters](blur-filters.md)
  Apply blurs, simulate motion and zoom effects, reduce noise, and erode and dilate image regions.
- [Color Adjustment Filters](color-adjustment-filters.md)
  Apply color transformations, including exposure, hue, and tint adjustments.
- [Color Effect Filters](color-effect-filters.md)
  Apply color effects, including photo effects, dithering, and color maps.
- [Composite Operations](composite-operations.md)
  Composite images by using a range of blend modes and compositing operators.
- [Convolution Filters](convolution-filters.md)
  Produce effects such as blurring, sharpening, edge detection, translation, and embossing.
- [Distortion Filters](distortion-filters.md)
  Apply distortion to images.
- [Generator Filters](generator-filters.md)
  Generate barcode, geometric, and special-effect images.
- [Geometry Adjustment Filters](geometry-adjustment-filters.md)
  Translate, scale, and rotate images in 2D and 3D.
- [Gradient Filters](gradient-filters.md)
  Generate linear and radial gradients.
- [Halftone Effect Filters](halftone-effect-filters.md)
  Simulate monochrome and CMYK halftone screens.
- [Reduction Filters](reduction-filters.md)
  Create statistical information about an image.
- [Sharpening Filters](sharpening-filters.md)
  Apply sharpening to images.
- [Stylizing Filters](stylizing-filters.md)
  Create stylized versions of images by applying effects including pixelation and line overlays.
- [Tile Effect Filters](tile-effect-filters.md)
  Produce tiled images from source images.
- [Transition Filters](transition-filters.md)
  Transition between two images by using effects including page curl and swipe.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilterprotocol)*