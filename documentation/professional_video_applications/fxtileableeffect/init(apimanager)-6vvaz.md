# init(apiManager:)

**Framework**: Professional Video Applications  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

Initializes the API manager for your plug-in.

**Availability**:
- FxPlug 4.0+

## Declaration

```swift
init?(apiManager: any PROAPIAccessing)
```

```objc
- (id) initWithAPIManager:(id<PROAPIAccessing>) apiManager;
```

## Mentions

- [Adding onscreen controls to plug-ins](https://developer.apple.com/documentation/professional-video-applications/adding-onscreen-controls-to-plug-ins)

#### Discussion

Save a weak reference to the `apiManager` object to use in subsequent calls. The plug-in initializes its properties and instance variables and returns a pointer to `self`. If any part of initialization fails in an unrecoverable way, this method returns `nil`.

## Parameters

- `apiManager`: An object that obtains the various API objects your plug-in will need for communicating with the host application.

## See Also

### Setting up your plug-in
- [protocol PROAPIAccessing](../proapiaccessing.md)
- [func finishInitialSetup() throws](./finishinitialsetup%28%29.md)
  Finishes the initial setup and is called exactly once on first application of your plug-in to allow it to do anything else it needs to in order to finish setting itself up.
- [func pluginInstanceAddedToDocument()](./plugininstanceaddedtodocument%28%29.md)
  Notifies your plug-in when it becomes part of user’s document.
- [func properties(AutoreleasingUnsafeMutablePointer<NSDictionary>?) throws](./properties%28_%29.md)
  Tells the host application about what the plug-in needs and supports, such as whether it renders in a gamma-corrected color space or a linear one.


---

*[View on Apple Developer](https://developer.apple.com/documentation/professional_video_applications/fxtileableeffect/init(apimanager:)-6vvaz)*