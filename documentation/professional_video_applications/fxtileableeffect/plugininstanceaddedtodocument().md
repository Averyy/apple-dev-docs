# pluginInstanceAddedToDocument()

**Framework**: Professional Video Applications  
**Kind**: method  
**Role**: Instance Method

Notifies your plug-in when it becomes part of user’s document.

**Availability**:
- FxPlug 4.2+

## Declaration

```swift
optional func pluginInstanceAddedToDocument()
```

```objc
- (void) pluginInstanceAddedToDocument;
```

#### Discussion

Called when a new plug-in instance is created or a document is loaded and an existing instance is deserialized. When the host calls this method, the plug-in is a part of the document and the various API objects work as expected.

## See Also

### Setting up your plug-in
- [init?(apiManager: any PROAPIAccessing)](./init%28apimanager%29-6vvaz.md)
  Initializes the API manager for your plug-in.
- [protocol PROAPIAccessing](../proapiaccessing.md)
- [func finishInitialSetup() throws](./finishinitialsetup%28%29.md)
  Finishes the initial setup and is called exactly once on first application of your plug-in to allow it to do anything else it needs to in order to finish setting itself up.
- [func properties(AutoreleasingUnsafeMutablePointer<NSDictionary>?) throws](./properties%28_%29.md)
  Tells the host application about what the plug-in needs and supports, such as whether it renders in a gamma-corrected color space or a linear one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/plugininstanceaddedtodocument())*