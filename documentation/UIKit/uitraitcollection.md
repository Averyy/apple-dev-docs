# UITraitCollection

**Framework**: UIKit  
**Kind**: class

A collection of data that represents the environment for an individual element in your app’s user interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class UITraitCollection
```

## Mentions

- [Providing data to the view hierarchy with custom traits](providing-data-to-the-view-hierarchy-with-custom-traits.md)
- [Building a desktop-class iPad app](building-a-desktop-class-ipad-app.md)
- [Displaying and managing views with a view controller](displaying-and-managing-views-with-a-view-controller.md)

#### Overview

The [`traitCollection`](uitraitenvironment/traitcollection.md) property of the [`UITraitEnvironment`](uitraitenvironment.md) protocol contains traits that describe the state of various elements of the iOS user interface, such as size class, display scale, and layout direction. Together, these traits compose the UIKit trait environment.

The following classes adopt [`UITraitEnvironment`](uitraitenvironment.md): [`UIScreen`](uiscreen.md), [`UIWindow`](uiwindow.md), [`UIWindowScene`](uiwindowscene.md), [`UIViewController`](uiviewcontroller.md), [`UIPresentationController`](uipresentationcontroller.md), and [`UIView`](uiview.md). To create an adaptive interface, write code to adjust your app’s layout according to changes in these traits. You access specific trait values using the [`UITraitCollection`](uitraitcollection.md) [`horizontalSizeClass`](uitraitcollection/horizontalsizeclass.md), [`verticalSizeClass`](uitraitcollection/verticalsizeclass.md), [`displayScale`](uitraitcollection/displayscale.md), [`userInterfaceIdiom`](uitraitcollection/userinterfaceidiom.md), and other properties.

To make your view controllers and views responsive to changes in the iOS interface environment, use automatic trait tracking in supported [`UIViewController`](uiviewcontroller.md) and [`UIView`](uiview.md) methods, or register to track specific trait changes with [`UITraitChangeObservable`](uitraitchangeobservable-67e94.md) methods. For more information, see [`Adapting your app when traits change`](adapting-your-app-when-traits-change.md).

To customize view controller animations in response to interface environment changes, override the [`willTransition(to:with:)`](uicontentcontainer/willtransition(to:with:).md) method of the [`UIContentContainer`](uicontentcontainer.md) protocol.

The following image shows the horizontal (width) and vertical (height) size classes your app can encounter when running full-screen on various devices.

![Examples of size classes on iOS devices. The top figures show the size classes for a 10.5 inch iPad as horizontally and vertically regular. For an iPhone X, the vertical size class in a portrait orientation is regular, but all of the other size classes are compact.](https://docs-assets.developer.apple.com/published/73a767796fad883938133c0fc1df95b4/media-2957521%402x.png)

You can create standalone trait collections to assist in matching against specific environments. The [`UITraitCollection`](uitraitcollection.md) class includes four specialized constructors, as well as a constructor that enables you to combine an array of trait collections, [`init(traitsFrom:)`](uitraitcollection/init(traitsfrom:).md).

One important use of standalone trait collections is to enable conditional use of images based on the current iOS interface environment. You can associate a trait collection with a [`UIImage`](uiimage.md) instance by way of a [`UIImageAsset`](uiimageasset.md) instance, as described in the overview section of [`UIImageAsset`](uiimageasset.md). For information on configuring asset catalogs graphically from within the Xcode IDE, see [`Managing assets with asset catalogs`](https://developer.apple.com/documentation/Xcode/managing-assets-with-asset-catalogs).

You can employ a standalone trait collection to enable a two-column split view in landscape orientation on iPhone. See the [`setOverrideTraitCollection(_:forChild:)`](uiviewcontroller/setoverridetraitcollection(_:forchild:).md) method of the [`UIViewController`](uiviewcontroller.md) class.

You can also use a standalone trait collection to customize view appearance with the [`appearance(for:)`](uiappearance/appearance(for:).md) protocol method, as described in [`UIAppearance`](uiappearance.md).

For information on creating custom traits, see [`Providing data to the view hierarchy with custom traits`](providing-data-to-the-view-hierarchy-with-custom-traits.md).

## Topics

### Getting the current traits
- [class var current: UITraitCollection](uitraitcollection/current.md)
  The trait collection for the current execution context.
### Getting related traits
- [static var systemTraitsAffectingColorAppearance: [UITrait]](uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md)
- [static var systemTraitsAffectingImageLookup: [UITrait]](uitraitcollection/systemtraitsaffectingimagelookup-4jv5.md)
### Modifying traits
- [convenience init(mutations: (inout any UIMutableTraits) -> Void)](uitraitcollection/init(mutations:).md)
- [func modifyingTraits((inout any UIMutableTraits) -> Void) -> UITraitCollection](uitraitcollection/modifyingtraits(_:).md)
- [UITraitCollection.TraitMutations](uitraitcollection/traitmutations.md)
### Getting trait changes
- [func changedTraits(from: UITraitCollection?) -> [UITrait]](uitraitcollection/changedtraits(from:).md)
### Comparing trait collections
- [func hasDifferentColorAppearance(comparedTo: UITraitCollection?) -> Bool](uitraitcollection/hasdifferentcolorappearance(comparedto:).md)
  Queries whether changing between the specified and current trait collections would affect color values.
- [func containsTraits(in: UITraitCollection?) -> Bool](uitraitcollection/containstraits(in:).md)
  Queries whether a trait collection contains all of another trait collection’s values.
### Performing actions with the current traits
- [func performAsCurrent(() -> Void)](uitraitcollection/performascurrent(_:).md)
  Executes custom code using the traits of the receiving trait collection.
### Retrieving size class traits
- [var horizontalSizeClass: UIUserInterfaceSizeClass](uitraitcollection/horizontalsizeclass.md)
  The horizontal size class of the trait collection.
- [var verticalSizeClass: UIUserInterfaceSizeClass](uitraitcollection/verticalsizeclass.md)
  The vertical size class of the trait collection.
- [enum UIUserInterfaceSizeClass](uiuserinterfacesizeclass.md)
  Constants that indicate the size class of a view.
### Retrieving display-related traits
- [var displayScale: CGFloat](uitraitcollection/displayscale.md)
  The display scale of the trait collection.
- [var displayGamut: UIDisplayGamut](uitraitcollection/displaygamut.md)
  The gamut of the current display.
- [enum UIDisplayGamut](uidisplaygamut.md)
  Constants that indicate the gamut of the current display.
### Retrieving interface-related traits
- [var userInterfaceStyle: UIUserInterfaceStyle](uitraitcollection/userinterfacestyle.md)
  The style associated with the user interface.
- [enum UIUserInterfaceStyle](uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](uitraitcollection/userinterfaceidiom.md)
  The user interface idiom of the trait collection.
- [enum UIUserInterfaceIdiom](uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [var userInterfaceLevel: UIUserInterfaceLevel](uitraitcollection/userinterfacelevel.md)
  The elevation level of the interface.
- [enum UIUserInterfaceLevel](uiuserinterfacelevel.md)
  Constants that indicate the visual level for content in the window.
- [var layoutDirection: UITraitEnvironmentLayoutDirection](uitraitcollection/layoutdirection.md)
  The layout direction associated with the current environment.
- [enum UITraitEnvironmentLayoutDirection](uitraitenvironmentlayoutdirection.md)
  Constants that indicate the layout direction associated with the current environment.
- [var resolvesNaturalAlignmentWithBaseWritingDirection: Bool](uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [var accessibilityContrast: UIAccessibilityContrast](uitraitcollection/accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [enum UIAccessibilityContrast](uiaccessibilitycontrast.md)
  Constants that indicate the accessibility contrast setting.
- [var legibilityWeight: UILegibilityWeight](uitraitcollection/legibilityweight.md)
  The font weight to apply to text.
- [enum UILegibilityWeight](uilegibilityweight.md)
  Constants that indicate the weight to apply to text in your interface.
- [var activeAppearance: UIUserInterfaceActiveAppearance](uitraitcollection/activeappearance.md)
  A property that indicates whether the user interface has an active appearance.
- [enum UIUserInterfaceActiveAppearance](uiuserinterfaceactiveappearance.md)
  Constants that indicate whether the user interface has an active appearance.
- [var toolbarItemPresentationSize: UINSToolbarItemPresentationSize](uitraitcollection/toolbaritempresentationsize.md)
  The presentation size of a toolbar item in an AppKit toolbar.
- [enum UINSToolbarItemPresentationSize](uinstoolbaritempresentationsize.md)
  Constants that specify the presentation size of a toolbar item in an AppKit toolbar.
- [var hdrHeadroomUsageLimit: UIHDRHeadroomUsageLimit](uitraitcollection/hdrheadroomusagelimit.md)
  If HDR headroom should be used for the current UI configuration. Headroom usage is disabled in certain UI configurations, such as when all an application’s windows are in the background.
- [enum UIHDRHeadroomUsageLimit](uihdrheadroomusagelimit.md)
### Retrieving the force touch capability traits
- [var forceTouchCapability: UIForceTouchCapability](uitraitcollection/forcetouchcapability.md)
  The force touch capability value of the trait collection.
- [enum UIForceTouchCapability](uiforcetouchcapability.md)
  Keys that indicate the availability of 3D Touch on a device.
### Retrieving content size category information
- [var preferredContentSizeCategory: UIContentSizeCategory](uitraitcollection/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [struct UIContentSizeCategory](uicontentsizecategory.md)
  Constants that indicate the preferred size of your content.
### Retrieving layout environment traits
- [var listEnvironment: UIListEnvironment](uitraitcollection/listenvironment.md)
- [enum UIListEnvironment](uilistenvironment.md)
  Constants that indicate the style of the containing list in a collection view or table view.
- [var splitViewControllerLayoutEnvironment: UISplitViewController.LayoutEnvironment](uitraitcollection/splitviewcontrollerlayoutenvironment.md)
  The split view controller layout environment represents whether an ancestor split view controller is expanded or collapsed.
- [UISplitViewController.LayoutEnvironment](uisplitviewcontroller/layoutenvironment.md)
  Constants that indicate the current layout of the containing split view controller.
- [var tabAccessoryEnvironment: UITabAccessory.Environment](uitraitcollection/tabaccessoryenvironment.md)
  The tab accessory environment represents whether a given trait collection is from a view in a `UITabAccessory` content view.
- [UITabAccessory.Environment](uitabaccessory/environment.md)
### Retrieving scene capture state
- [var sceneCaptureState: UISceneCaptureState](uitraitcollection/scenecapturestate.md)
- [enum UISceneCaptureState](uiscenecapturestate.md)
### Retrieving dynamic range traits
- [var imageDynamicRange: UIImage.DynamicRange](uitraitcollection/imagedynamicrange.md)
### Retrieving typesetting language traits
- [var typesettingLanguage: Locale.Language?](uitraitcollection/typesettinglanguage-6i635.md)
### Getting an image configuration object
- [var imageConfiguration: UIImage.Configuration](uitraitcollection/imageconfiguration.md)
  An image configuration object compatible with this trait collection.
### Creating a trait collection
- [init()](uitraitcollection/init.md)
  Creates a trait collection whose traits are set to their default (unspecified) values.
- [init(userInterfaceIdiom: UIUserInterfaceIdiom)](uitraitcollection/init(userinterfaceidiom:).md)
  Creates a trait collection that contains only a specified interface idiom.
- [init(horizontalSizeClass: UIUserInterfaceSizeClass)](uitraitcollection/init(horizontalsizeclass:).md)
  Creates a trait collection that contains only a specified horizontal size class.
- [init(verticalSizeClass: UIUserInterfaceSizeClass)](uitraitcollection/init(verticalsizeclass:).md)
  Creates a trait collection that contains only a specified vertical size class.
- [init(userInterfaceStyle: UIUserInterfaceStyle)](uitraitcollection/init(userinterfacestyle:).md)
  Creates a trait collection that contains only the specified user interface style trait.
- [init(accessibilityContrast: UIAccessibilityContrast)](uitraitcollection/init(accessibilitycontrast:).md)
  Creates a trait collection that contains only the specified accessibility contrast trait.
- [init(userInterfaceLevel: UIUserInterfaceLevel)](uitraitcollection/init(userinterfacelevel:).md)
  Creates a trait collection that contains only the specified user interface level trait.
- [init(legibilityWeight: UILegibilityWeight)](uitraitcollection/init(legibilityweight:).md)
  Creates a trait collection that contains only the specified legibility weight trait.
- [init(forceTouchCapability: UIForceTouchCapability)](uitraitcollection/init(forcetouchcapability:).md)
  Creates a trait collection that contains only a specified force touch capability trait.
- [init(displayScale: CGFloat)](uitraitcollection/init(displayscale:).md)
  Creates a trait collection that contains only a specified display scale.
- [init(displayGamut: UIDisplayGamut)](uitraitcollection/init(displaygamut:).md)
  Creates a trait collection that contains only the specified display gamut trait.
- [init(layoutDirection: UITraitEnvironmentLayoutDirection)](uitraitcollection/init(layoutdirection:).md)
  Creates a trait collection that contains only the specified layout direction trait.
- [init(preferredContentSizeCategory: UIContentSizeCategory)](uitraitcollection/init(preferredcontentsizecategory:).md)
  Creates a trait collection that contains only the specified content size category trait.
- [init(activeAppearance: UIUserInterfaceActiveAppearance)](uitraitcollection/init(activeappearance:).md)
  Creates a trait collection that contains only the specified active appearance trait.
- [init(toolbarItemPresentationSize: UINSToolbarItemPresentationSize)](uitraitcollection/init(toolbaritempresentationsize:).md)
  Creates a trait collection that contains only the specified toolbar item presentation size trait.
- [init(hdrHeadroomUsageLimit: UIHDRHeadroomUsageLimit)](uitraitcollection/init(hdrheadroomusagelimit:).md)
- [init(imageDynamicRange: UIImage.DynamicRange)](uitraitcollection/init(imagedynamicrange:).md)
- [init(listEnvironment: UIListEnvironment)](uitraitcollection/init(listenvironment:).md)
- [convenience init(resolvesNaturalAlignmentWithBaseWritingDirection: Bool)](uitraitcollection/init(resolvesnaturalalignmentwithbasewritingdirection:).md)
- [init(sceneCaptureState: UISceneCaptureState)](uitraitcollection/init(scenecapturestate:).md)
- [init(tabAccessoryEnvironment: UITabAccessory.Environment)](uitraitcollection/init(tabaccessoryenvironment:).md)
  Constructs a new trait collection with the given `tabAccessoryEnvironment`.
- [convenience init(typesettingLanguage: Locale.Language?)](uitraitcollection/init(typesettinglanguage:).md)
- [init?(coder: NSCoder)](uitraitcollection/init(coder:).md)
  Creates a trait collection from data in an unarchiver.
- [init(traitsFrom: [UITraitCollection])](uitraitcollection/init(traitsfrom:).md)
  Creates a trait collection that consists of traits merged from a specified array of trait collections.
### Initializers
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-3as8f.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-3fg2.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-4100d.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-48zja.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-4shto.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-4slti.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-55rvq.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-58ia2.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-59di1.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-59u4e.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-6h22m.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-7sd52.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-7toc9.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-836bk.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-8k1t1.md)
- [convenience init<T>(T.Type, value: T.Value)](uitraitcollection/init(_:value:)-vvgw.md)
### Instance Methods
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-162et.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-1n0uk.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-1wvrv.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-227ps.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-3p47.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-418p6.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-4c3s8.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-5swjm.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-7jssv.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-8gf97.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-8yat4.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-8z10u.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-8z152.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-8zl00.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-9op5s.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](uitraitcollection/replacing(_:value:)-o6qa.md)
### Subscripts
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-10ujz.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-1kkve.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-1n030.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-2bvk.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-32r6h.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-3ztj.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-43in7.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-4gjs6.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-4zpi4.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-5wwet.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-6cdgq.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-6jr9c.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-8rqo4.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-90z0t.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-96v58.md)
- [subscript<T>(T.Type) -> T.Value](uitraitcollection/subscript(_:)-9nfd8.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol UITraitEnvironment](uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [Automatic trait tracking](automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [protocol UIAdaptivePresentationControllerDelegate](uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [protocol UIContentContainer](uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection)*