# Storyboard support

**Framework**: Watchkit

Connect your code to storyboard elements using interface controllers, interface objects, and event handlers.

## Overview

The WatchKit framework includes classes to control user interface elements that you lay out in your storyboard. Storyboard-based layouts typically require an interface controller for each scene. Each controller can manage one or more controls and subviews, such as tables, buttons, sliders, and other visual elements. Use the classes in this collection to configure your visual elements at runtime, and to respond to user interactions.

> **Note**:  When you build the user interface for your watchOS app, you can design the interface in a storyboard and use WatchKit classes to connect to the interface elements, or you can use SwiftUI to declare the interface in code. Because apps built with SwiftUI have more freedom, power, and control over the user interface than apps designed in a storyboard, strongly consider using SwiftUI when creating your watchOS app. For more information, see `Building a watchOS App`.

 When you build the user interface for your watchOS app, you can design the interface in a storyboard and use WatchKit classes to connect to the interface elements, or you can use SwiftUI to declare the interface in code. Because apps built with SwiftUI have more freedom, power, and control over the user interface than apps designed in a storyboard, strongly consider using SwiftUI when creating your watchOS app. For more information, see `Building a watchOS App`.

## Topics

### User interface basics
- [Building watchOS app Interfaces Using the Storyboard](building-watchos-app-interfaces-using-the-storyboard.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/building-watchos-app-interfaces-using-the-storyboard))
  Create the user interface for your watchOS app by nesting stacks.
- [class WKInterfaceObject](wkinterfaceobject.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceobject))
  An object that provides information that is common to all interface objects in your watchOS app.
- [class WKInterfaceController](wkinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacecontroller))
  A class that provides the infrastructure for managing the interface in a watchOS app.
- [class WKAlertAction](wkalertaction.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkalertaction))
  An object that encapsulates information about a button displayed in an alert or action sheet.
- [class WKAccessibilityImageRegion](wkaccessibilityimageregion.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityimageregion))
  An object that defines a portion of an image that you want to call out separately to an assistive app.
- [func WKAccessibilityIsVoiceOverRunning() -> Bool](wkaccessibilityisvoiceoverrunning().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisvoiceoverrunning()))
  Returns a Boolean value indicating whether VoiceOver is running.
- [func WKAccessibilityIsReduceMotionEnabled() -> Bool](wkaccessibilityisreducemotionenabled().md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaccessibilityisreducemotionenabled()))
  Returns a Boolean value indicating whether reduced motion is enabled.
### Controls
- [class WKInterfaceLabel](wkinterfacelabel.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacelabel))
  An interface element that displays static text.
- [class WKInterfaceDate](wkinterfacedate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacedate))
  A label that displays the current date or time.
- [class WKInterfaceTimer](wkinterfacetimer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetimer))
  A label that displays a countdown or count-up timer.
- [class WKInterfaceButton](wkinterfacebutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacebutton))
  A button in the user interface of your watchOS app.
- [class WKInterfaceAuthorizationAppleIDButton](wkinterfaceauthorizationappleidbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceauthorizationappleidbutton))
  A button that you can use to trigger a Sign in with Apple request.
- [class WKInterfacePaymentButton](wkinterfacepaymentbutton.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton))
  A button that you can use to trigger payments through Apple Pay.
- [class WKInterfaceTextField](wkinterfacetextfield.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetextfield))
  An interface element that displays an editable text area.
- [class WKInterfaceSwitch](wkinterfaceswitch.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceswitch))
  An interface element that toggles between an On and Off state.
- [class WKInterfaceSlider](wkinterfaceslider.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceslider))
  An interface element that lets users select a single floating-point value from a range of values.
- [class WKInterfaceActivityRing](wkinterfaceactivityring.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceactivityring))
  A view that displays data from a HealthKit activity summary object.
- [class WKInterfaceMap](wkinterfacemap.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemap))
  An interface element that displays a noninteractive map for the location you specify.
### Containers
- [class WKInterfaceGroup](wkinterfacegroup.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacegroup))
  A container for one or more interface objects.
- [class WKInterfaceSeparator](wkinterfaceseparator.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceseparator))
  An interface object that displays a visual separator within a group.
- [class WKInterfaceTable](wkinterfacetable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacetable))
  An object that creates and manages the contents of a single-column table interface.
- [class WKInterfacePicker](wkinterfacepicker.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacepicker))
  An interface element that presents a scrolling list of items for the user to choose from.
### Audio
- [Playing Background Audio](playing-background-audio.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/playing-background-audio))
  Enable background audio in your app to provide a seamless playback experience.
- [Adding a Now Playing View](adding-a-now-playing-view.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/adding-a-now-playing-view))
  Provide a view that controls the currently playing audio from your app.
- [class WKInterfaceVolumeControl](wkinterfacevolumecontrol.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacevolumecontrol))
  An interface element that provides control of the audio volume from the watch or a paired iPhone.
- PUICAutoLaunchAudioOptOut ([Apple Docs](https://developer.apple.com/documentation/BundleResources/Information-Property-List/PUICAutoLaunchAudioOptOut))
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [class WKAudioFilePlayer](wkaudiofileplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayer))
  An object that controls playback of a single audio item.
- [class WKAudioFileQueuePlayer](wkaudiofilequeueplayer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofilequeueplayer))
  An object that controls playback of one or more audio items.
- [class WKAudioFilePlayerItem](wkaudiofileplayeritem.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileplayeritem))
  An object that manages the presentation state of an audio file while it is playing.
- [class WKAudioFileAsset](wkaudiofileasset.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkaudiofileasset))
  An object that stores a reference to an audio file and provides metadata information about that file.
### Images and movies
- [class WKInterfaceImage](wkinterfaceimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceimage))
  An image that can be displayed in the interface of your watchOS app.
- [class WKImage](wkimage.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimage))
  A wrapper for images you use with a picker interface.
- [protocol WKImageAnimatable](wkimageanimatable.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkimageanimatable))
  A collection of methods you can use to control the playback of animated images.
- [class WKInterfaceMovie](wkinterfacemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacemovie))
  An interface element that lets you play video and audio content in your watchOS app.
- [class WKInterfaceInlineMovie](wkinterfaceinlinemovie.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceinlinemovie))
  An interface element that displays a video’s poster image and supports inline playing of the video.
- [class WKInterfaceHMCamera](wkinterfacehmcamera.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacehmcamera))
  An interface element that displays either a video stream or a single snapshot from an IP camera connected to HomeKit.
- [enum WKVideoGravity](wkvideogravity.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkvideogravity))
  Constants indicating the appearance of video content.
### Graphics and games
- [class WKInterfaceSKScene](wkinterfaceskscene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfaceskscene))
  A visual WatchKit element that displays a SpriteKit scene.
- [class WKInterfaceSCNScene](wkinterfacescnscene.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkinterfacescnscene))
  An object that lets you manage SceneKit content for display in your app.
### Event handling
- [class WKCrownSequencer](wkcrownsequencer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrownsequencer))
  An object that reports the current state of the digital crown, including its rotational speed when it is in motion.
- [protocol WKCrownDelegate](wkcrowndelegate.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkcrowndelegate))
  A collection of methods you can implement to track the user’s interaction with the digital crown, receiving notifications when the user rotates the crown or when rotation stops.
- [class WKGestureRecognizer](wkgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkgesturerecognizer))
  The base class for all other gesture recognizer classes.
- [class WKLongPressGestureRecognizer](wklongpressgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wklongpressgesturerecognizer))
  A gesture recognizer that interprets a touch event that occurs in the same relative area for an extended period of time.
- [class WKPanGestureRecognizer](wkpangesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkpangesturerecognizer))
  A gesture recognizer that interprets a touch event that moves around the screen.
- [class WKSwipeGestureRecognizer](wkswipegesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkswipegesturerecognizer))
  A gesture recognizer that interprets swiping gestures in one or more directions.
- [class WKTapGestureRecognizer](wktapgesturerecognizer.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wktapgesturerecognizer))
  A gesture recognizer that interprets a touch event occurring and ending in approximately the same area on the screen.
### Notifications
- [class WKUserNotificationInterfaceController](wkusernotificationinterfacecontroller.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/wkusernotificationinterfacecontroller))
  An interface controller object that manages a dynamic user interface for a local or remote notification.

## See Also

- [struct NowPlayingView](nowplayingview.md) ([Apple Docs](https://developer.apple.com/documentation/watchkit/nowplayingview))


---

*[View on Apple Developer](https://developer.apple.com/documentation/watchkit/storyboard-support)*