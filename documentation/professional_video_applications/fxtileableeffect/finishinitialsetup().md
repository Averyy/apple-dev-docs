# finishInitialSetup()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Finishes the initial setup and is called exactly once on first application of your plug-in to allow it to do anything else it needs to in order to finish setting itself up.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
optional func finishInitialSetup() throws
```

```objc
- (BOOL) finishInitialSetup:(NSError * *) error;
```

## Discussion

This is called after [`init(apiManager:)`](./init%28apimanager%29-6vvaz.md), [`addParameters()`](./addparameters%28%29.md), and [`properties(_:)`](./properties%28_%29.md).

> **Note**:  This method will never be called by Final Cut Pro as it was called when the plug-in was initially added to the template in Motion.

## See Also

### Setting up your plug-in
- [init?(apiManager: any PROAPIAccessing)](./init%28apimanager%29-6vvaz.md)
  Initializes the API manager for your plug-in.
- [protocol PROAPIAccessing](../proapiaccessing.md)
- [func pluginInstanceAddedToDocument()](./plugininstanceaddedtodocument%28%29.md)
  Notifies your plug-in when it becomes part of user’s document.
- [func properties(AutoreleasingUnsafeMutablePointer<NSDictionary>?) throws](./properties%28_%29.md)
  Tells the host application about what the plug-in needs and supports, such as whether it renders in a gamma-corrected color space or a linear one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/finishinitialsetup())*