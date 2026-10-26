# UITraitCollection

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A collection of data that represents the environment for an individual element in your app’s user interface.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
class UITraitCollection
```

```objc
@interface UITraitCollection : NSObject
```

## Mentions

- [Providing data to the view hierarchy with custom traits](./providing-data-to-the-view-hierarchy-with-custom-traits.md)
- [Building a desktop-class iPad app](./building-a-desktop-class-ipad-app.md)
- [Displaying and managing views with a view controller](./displaying-and-managing-views-with-a-view-controller.md)

#### Overview

The [`traitCollection`](./uitraitenvironment/traitcollection.md) property of the [`UITraitEnvironment`](./uitraitenvironment.md) protocol contains traits that describe the state of various elements of the iOS user interface, such as size class, display scale, and layout direction. Together, these traits compose the UIKit trait environment.

The following classes adopt [`UITraitEnvironment`](./uitraitenvironment.md): [`UIScreen`](./uiscreen.md), [`UIWindow`](./uiwindow.md), [`UIWindowScene`](./uiwindowscene.md), [`UIViewController`](./uiviewcontroller.md), [`UIPresentationController`](./uipresentationcontroller.md), and [`UIView`](./uiview.md). To create an adaptive interface, write code to adjust your app’s layout according to changes in these traits. You access specific trait values using the [`UITraitCollection`](./uitraitcollection.md) [`horizontalSizeClass`](./uitraitcollection/horizontalsizeclass.md), [`verticalSizeClass`](./uitraitcollection/verticalsizeclass.md), [`displayScale`](./uitraitcollection/displayscale.md), [`userInterfaceIdiom`](./uitraitcollection/userinterfaceidiom.md), and other properties.

To make your view controllers and views responsive to changes in the iOS interface environment, use automatic trait tracking in supported [`UIViewController`](./uiviewcontroller.md) and [`UIView`](./uiview.md) methods, or register to track specific trait changes with [`UITraitChangeObservable`](./uitraitchangeobservable-67e94.md) methods. For more information, see [Adapting your app when traits change](./adapting-your-app-when-traits-change.md).

To customize view controller animations in response to interface environment changes, override the [`willTransition(to:with:)`](./uicontentcontainer/willtransition%28to,with%29.md) method of the [`UIContentContainer`](./uicontentcontainer.md) protocol.

For more information about the horizontal (width) and vertical (height) size classes your app can encounter when running full-screen on various devices, see Human Interface Guidelines > [Layout](https://developer.apple.com/design/human-interface-guidelines/layout).

You can create standalone trait collections to assist in matching against specific environments. The [`UITraitCollection`](./uitraitcollection.md) class includes four specialized constructors, as well as a constructor that enables you to combine an array of trait collections, [`init(traitsFrom:)`](./uitraitcollection/init%28traitsfrom%29.md).

One important use of standalone trait collections is to enable conditional use of images based on the current iOS interface environment. You can associate a trait collection with a [`UIImage`](./uiimage.md) instance by way of a [`UIImageAsset`](./uiimageasset.md) instance, as described in the overview section of [`UIImageAsset`](./uiimageasset.md). For information on configuring asset catalogs graphically from within the Xcode IDE, see [Managing assets with asset catalogs](../Xcode/managing-assets-with-asset-catalogs.md).

You can employ a standalone trait collection to enable a two-column split view in landscape orientation on iPhone. See the [`setOverrideTraitCollection(_:forChild:)`](./uiviewcontroller/setoverridetraitcollection%28_,forchild%29.md) method of the [`UIViewController`](./uiviewcontroller.md) class.

You can also use a standalone trait collection to customize view appearance with the [`appearance(for:)`](./uiappearance/appearance%28for%29.md) protocol method, as described in [`UIAppearance`](./uiappearance.md).

For information on creating custom traits, see [Providing data to the view hierarchy with custom traits](./providing-data-to-the-view-hierarchy-with-custom-traits.md).

## Topics

### Getting the current traits
- [class var current: UITraitCollection](./uitraitcollection/current.md)
  The trait collection for the current execution context.
### Getting related traits
- [static var systemTraitsAffectingColorAppearance: [UITrait]](./uitraitcollection/systemtraitsaffectingcolorappearance-64z7q.md)
- [static var systemTraitsAffectingImageLookup: [UITrait]](./uitraitcollection/systemtraitsaffectingimagelookup-4jv5.md)
- [static var systemTraitsAffectingVerticalBarEdge: [UITrait]](./uitraitcollection/systemtraitsaffectingverticalbaredge-475st.md)
  The system traits that affect the value of `verticalBarEdge`.
- [systemTraitsAffectingColorAppearance](./uitraitcollection/systemtraitsaffectingcolorappearance-18zhm.md)
- [systemTraitsAffectingImageLookup](./uitraitcollection/systemtraitsaffectingimagelookup-640w8.md)
- [systemTraitsAffectingVerticalBarEdge](./uitraitcollection/systemtraitsaffectingverticalbaredge-8k87m.md)
  The system traits that affect the value of `verticalBarEdge`.
### Modifying traits
- [convenience init(mutations: UITraitCollection.TraitMutations)](./uitraitcollection/init%28mutations%29.md)
- [func modifyingTraits(UITraitCollection.TraitMutations) -> UITraitCollection](./uitraitcollection/modifyingtraits%28_%29.md)
- [UITraitCollection.TraitMutations](./uitraitcollection/traitmutations.md)
- [+ traitCollectionWithTraits:](./uitraitcollection/traitcollectionwithtraits_.md)
- [- traitCollectionByModifyingTraits:](./uitraitcollection/traitcollectionbymodifyingtraits_.md)
- [UITraitMutations](./uitraitmutations.md)
### Getting trait changes
- [func changedTraits(from: UITraitCollection?) -> [UITrait]](./uitraitcollection/changedtraits%28from%29.md)
### Comparing trait collections
- [func hasDifferentColorAppearance(comparedTo: UITraitCollection?) -> Bool](./uitraitcollection/hasdifferentcolorappearance%28comparedto%29.md)
  Queries whether changing between the specified and current trait collections would affect color values.
### Performing actions with the current traits
- [func performAsCurrent(() -> Void)](./uitraitcollection/performascurrent%28_%29.md)
  Executes custom code using the traits of the receiving trait collection.
### Retrieving size class traits
- [var horizontalSizeClass: UIUserInterfaceSizeClass](./uitraitcollection/horizontalsizeclass.md)
  The horizontal size class of the trait collection.
- [var verticalSizeClass: UIUserInterfaceSizeClass](./uitraitcollection/verticalsizeclass.md)
  The vertical size class of the trait collection.
- [enum UIUserInterfaceSizeClass](./uiuserinterfacesizeclass.md)
  Constants that indicate the size class of a view.
### Retrieving display-related traits
- [var displayScale: CGFloat](./uitraitcollection/displayscale.md)
  The display scale of the trait collection.
- [var displayGamut: UIDisplayGamut](./uitraitcollection/displaygamut.md)
  The gamut of the current display.
- [enum UIDisplayGamut](./uidisplaygamut.md)
  Constants that indicate the gamut of the current display.
### Retrieving interface-related traits
- [var userInterfaceStyle: UIUserInterfaceStyle](./uitraitcollection/userinterfacestyle.md)
  The style associated with the user interface.
- [enum UIUserInterfaceStyle](./uiuserinterfacestyle.md)
  Constants that indicate the interface style for the app.
- [var userInterfaceIdiom: UIUserInterfaceIdiom](./uitraitcollection/userinterfaceidiom.md)
  The user interface idiom of the trait collection.
- [enum UIUserInterfaceIdiom](./uiuserinterfaceidiom.md)
  Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [var userInterfaceLevel: UIUserInterfaceLevel](./uitraitcollection/userinterfacelevel.md)
  The elevation level of the interface.
- [enum UIUserInterfaceLevel](./uiuserinterfacelevel.md)
  Constants that indicate the visual level for content in the window.
- [var layoutDirection: UITraitEnvironmentLayoutDirection](./uitraitcollection/layoutdirection.md)
  The layout direction associated with the current environment.
- [enum UITraitEnvironmentLayoutDirection](./uitraitenvironmentlayoutdirection.md)
  Constants that indicate the layout direction associated with the current environment.
- [var resolvesNaturalAlignmentWithBaseWritingDirection: Bool](./uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [var accessibilityContrast: UIAccessibilityContrast](./uitraitcollection/accessibilitycontrast.md)
  The accessibility contrast associated with the current environment.
- [enum UIAccessibilityContrast](./uiaccessibilitycontrast.md)
  Constants that indicate the accessibility contrast setting.
- [var legibilityWeight: UILegibilityWeight](./uitraitcollection/legibilityweight.md)
  The font weight to apply to text.
- [enum UILegibilityWeight](./uilegibilityweight.md)
  Constants that indicate the weight to apply to text in your interface.
- [var activeAppearance: UIUserInterfaceActiveAppearance](./uitraitcollection/activeappearance.md)
  A property that indicates whether a scene has an active appearance.
- [enum UIUserInterfaceActiveAppearance](./uiuserinterfaceactiveappearance.md)
  Constants that indicate whether the user interface has an active appearance.
- [var toolbarItemPresentationSize: UINSToolbarItemPresentationSize](./uitraitcollection/toolbaritempresentationsize.md)
  The presentation size of a toolbar item in an AppKit toolbar.
- [enum UINSToolbarItemPresentationSize](./uinstoolbaritempresentationsize.md)
  Constants that specify the presentation size of a toolbar item in an AppKit toolbar.
- [var hdrHeadroomUsageLimit: UIHDRHeadroomUsageLimit](./uitraitcollection/hdrheadroomusagelimit.md)
  If HDR headroom should be used for the current UI configuration. Headroom usage is disabled in certain UI configurations, such as when all an application’s windows are in the background.
- [enum UIHDRHeadroomUsageLimit](./uihdrheadroomusagelimit.md)
- [var verticalBarEdge: UIVerticalBarEdge](./uitraitcollection/verticalbaredge.md)
  The edge where the system places the vertical bar.
- [enum UIVerticalBarEdge](./uiverticalbaredge.md)
  The edge where the system places the vertical bar.
- [resolvesNaturalAlignmentWithBaseWritingDirection](./uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-97osy.md)
  Specifies the behavior for resolving `NSTextAlignment.natural` to the visual alignment.
### Retrieving the force touch capability traits
- [var forceTouchCapability: UIForceTouchCapability](./uitraitcollection/forcetouchcapability.md)
  The force touch capability value of the trait collection.
- [enum UIForceTouchCapability](./uiforcetouchcapability.md)
  Keys that indicate the availability of 3D Touch on a device.
### Retrieving content size category information
- [var preferredContentSizeCategory: UIContentSizeCategory](./uitraitcollection/preferredcontentsizecategory.md)
  The font sizing option preferred by the user.
- [struct UIContentSizeCategory](./uicontentsizecategory.md)
  Constants that indicate the preferred size of your content.
- [UIContentSizeCategoryCompareToCategory](./uicontentsizecategorycomparetocategory.md)
  Compares two content size category values to determine whether they are equal or whether one is larger than the other.
- [UIContentSizeCategoryIsAccessibilityCategory](./uicontentsizecategoryisaccessibilitycategory.md)
  Returns a Boolean value that indicates whether the content size category belongs to the group of accessibility-related sizes.
### Retrieving layout environment traits
- [var listEnvironment: UIListEnvironment](./uitraitcollection/listenvironment.md)
  The list environment represents whether a given trait collection is from a view in a UITableView or a UICollectionView list section.
- [enum UIListEnvironment](./uilistenvironment.md)
  Constants that indicate the style of the containing list in a collection view or table view.
- [var splitViewControllerLayoutEnvironment: UISplitViewController.LayoutEnvironment](./uitraitcollection/splitviewcontrollerlayoutenvironment.md)
  The split view controller layout environment represents whether an ancestor split view controller is expanded or collapsed.
- [UISplitViewController.LayoutEnvironment](./uisplitviewcontroller/layoutenvironment.md)
  Constants that indicate the current layout of the containing split view controller.
- [var tabAccessoryEnvironment: UITabAccessory.Environment](./uitraitcollection/tabaccessoryenvironment.md)
  The tab accessory environment represents whether a given trait collection is from a view in a `UITabAccessory` content view.
- [UITabAccessory.Environment](./uitabaccessory/environment.md)
### Retrieving scene capture state
- [var sceneCaptureState: UISceneCaptureState](./uitraitcollection/scenecapturestate.md)
  Scene capture state represents whether a scene is currently being mirrored or recorded.
- [enum UISceneCaptureState](./uiscenecapturestate.md)
### Retrieving dynamic range traits
- [var imageDynamicRange: UIImage.DynamicRange](./uitraitcollection/imagedynamicrange.md)
  The imageDynamicRange determines how HDR images will render in the given trait environment. SDR images are unaffected.
### Retrieving typesetting language traits
- [var typesettingLanguage: Locale.Language?](./uitraitcollection/typesettinglanguage-6i635.md)
- [typesettingLanguage](./uitraitcollection/typesettinglanguage-1n1fs.md)
### Getting an image configuration object
- [var imageConfiguration: UIImage.Configuration](./uitraitcollection/imageconfiguration.md)
  An image configuration object compatible with this trait collection.
### Creating a trait collection
- [init()](./uitraitcollection/init%28%29.md)
  Creates a trait collection whose traits are set to their default (unspecified) values.
- [init(userInterfaceIdiom: UIUserInterfaceIdiom)](./uitraitcollection/init%28userinterfaceidiom%29.md)
  Creates a trait collection that contains only a specified interface idiom.
- [init(horizontalSizeClass: UIUserInterfaceSizeClass)](./uitraitcollection/init%28horizontalsizeclass%29.md)
  Creates a trait collection that contains only a specified horizontal size class.
- [init(verticalSizeClass: UIUserInterfaceSizeClass)](./uitraitcollection/init%28verticalsizeclass%29.md)
  Creates a trait collection that contains only a specified vertical size class.
- [init(userInterfaceStyle: UIUserInterfaceStyle)](./uitraitcollection/init%28userinterfacestyle%29.md)
  Creates a trait collection that contains only the specified user interface style trait.
- [init(accessibilityContrast: UIAccessibilityContrast)](./uitraitcollection/init%28accessibilitycontrast%29.md)
  Creates a trait collection that contains only the specified accessibility contrast trait.
- [init(userInterfaceLevel: UIUserInterfaceLevel)](./uitraitcollection/init%28userinterfacelevel%29.md)
  Creates a trait collection that contains only the specified user interface level trait.
- [init(legibilityWeight: UILegibilityWeight)](./uitraitcollection/init%28legibilityweight%29.md)
  Creates a trait collection that contains only the specified legibility weight trait.
- [init(forceTouchCapability: UIForceTouchCapability)](./uitraitcollection/init%28forcetouchcapability%29.md)
  Creates a trait collection that contains only a specified force touch capability trait.
- [init(displayScale: CGFloat)](./uitraitcollection/init%28displayscale%29.md)
  Creates a trait collection that contains only a specified display scale.
- [init(displayGamut: UIDisplayGamut)](./uitraitcollection/init%28displaygamut%29.md)
  Creates a trait collection that contains only the specified display gamut trait.
- [init(layoutDirection: UITraitEnvironmentLayoutDirection)](./uitraitcollection/init%28layoutdirection%29.md)
  Creates a trait collection that contains only the specified layout direction trait.
- [init(preferredContentSizeCategory: UIContentSizeCategory)](./uitraitcollection/init%28preferredcontentsizecategory%29.md)
  Creates a trait collection that contains only the specified content size category trait.
- [init(activeAppearance: UIUserInterfaceActiveAppearance)](./uitraitcollection/init%28activeappearance%29.md)
  Creates a trait collection that contains only the specified active appearance trait.
- [init(toolbarItemPresentationSize: UINSToolbarItemPresentationSize)](./uitraitcollection/init%28toolbaritempresentationsize%29.md)
  Creates a trait collection that contains only the specified toolbar item presentation size trait.
- [init(hdrHeadroomUsageLimit: UIHDRHeadroomUsageLimit)](./uitraitcollection/init%28hdrheadroomusagelimit%29-5zqph.md)
- [init(imageDynamicRange: UIImage.DynamicRange)](./uitraitcollection/init%28imagedynamicrange%29.md)
  Construct a new trait collection with the given image content dynamic range.
- [init(listEnvironment: UIListEnvironment)](./uitraitcollection/init%28listenvironment%29.md)
  Construct a new trait collection with the given `listEnvironment`.
- [convenience init(resolvesNaturalAlignmentWithBaseWritingDirection: Bool)](./uitraitcollection/init%28resolvesnaturalalignmentwithbasewritingdirection%29.md)
- [init(sceneCaptureState: UISceneCaptureState)](./uitraitcollection/init%28scenecapturestate%29.md)
  Construct a new trait collection with the given scene capture state.
- [init(tabAccessoryEnvironment: UITabAccessory.Environment)](./uitraitcollection/init%28tabaccessoryenvironment%29.md)
  Constructs a new trait collection with the given `tabAccessoryEnvironment`.
- [convenience init(typesettingLanguage: Locale.Language?)](./uitraitcollection/init%28typesettinglanguage%29.md)
- [init?(coder: NSCoder)](./uitraitcollection/init%28coder%29.md)
  Creates a trait collection from data in an unarchiver.
### Deprecated
- [func containsTraits(in: UITraitCollection?) -> Bool](./uitraitcollection/containstraits%28in%29.md)
  Queries whether a trait collection contains all of another trait collection’s values.
- [init(traitsFrom: [UITraitCollection])](./uitraitcollection/init%28traitsfrom%29.md)
  Creates a trait collection that consists of traits merged from a specified array of trait collections.
- [init(traitsFromCollections: [UITraitCollection])](./uitraitcollection/init%28traitsfromcollections%29.md)
### Initializers
- [init(HDRHeadroomUsageLimit: UIHDRHeadroomUsageLimit)](./uitraitcollection/init%28hdrheadroomusagelimit%29-3nnko.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-3as8f.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-3fg2.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-4100d.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-48zja.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-4shto.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-4slti.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-55rvq.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-58ia2.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-59di1.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-59u4e.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-6h22m.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-7sd52.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-7toc9.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-836bk.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-8k1t1.md)
- [convenience init<T>(T.Type, value: T.Value)](./uitraitcollection/init%28_,value%29-vvgw.md)
- [convenience init(systemPrefersReducedResourceUsage: Bool)](./uitraitcollection/init%28systemprefersreducedresourceusage%29.md)
### Instance Properties
- [var navigationTitleAlignment: UINavigationItem.TitleAlignment](./uitraitcollection/navigationtitlealignment.md)
  The alignment the navigation bar resolved for its title.
- [var systemPrefersReducedResourceUsage: Bool](./uitraitcollection/systemprefersreducedresourceusage-1yl57.md)
- [systemPrefersReducedResourceUsage](./uitraitcollection/systemprefersreducedresourceusage-4szzj.md)
  A Boolean value that indicates whether the system prefers that the app reduce its resource usage.
### Instance Methods
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-162et.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-1n0uk.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-1wvrv.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-227ps.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-3p47.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-418p6.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-4c3s8.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-5swjm.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-7jssv.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-8gf97.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-8yat4.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-8z10u.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-8z152.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-8zl00.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-9op5s.md)
- [func replacing<T>(T.Type, value: T.Value) -> UITraitCollection](./uitraitcollection/replacing%28_,value%29-o6qa.md)
- [- changedTraitsFromTraitCollection:](./uitraitcollection/changedtraitsfromtraitcollection_.md)
- [- objectForTrait:](./uitraitcollection/objectfortrait_.md)
- [- traitCollectionByReplacingCGFloatValue:forTrait:](./uitraitcollection/traitcollectionbyreplacingcgfloatvalue_fortrait_.md)
- [- traitCollectionByReplacingNSIntegerValue:forTrait:](./uitraitcollection/traitcollectionbyreplacingnsintegervalue_fortrait_.md)
- [- traitCollectionByReplacingObject:forTrait:](./uitraitcollection/traitcollectionbyreplacingobject_fortrait_.md)
- [- valueForCGFloatTrait:](./uitraitcollection/valueforcgfloattrait_.md)
- [- valueForNSIntegerTrait:](./uitraitcollection/valuefornsintegertrait_.md)
### Subscripts
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-10ujz.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-1kkve.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-1n030.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-2bvk.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-32r6h.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-3ztj.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-43in7.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-4gjs6.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-4zpi4.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-5wwet.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-6cdgq.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-6jr9c.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-8rqo4.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-90z0t.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-96v58.md)
- [subscript<T>(T.Type) -> T.Value](./uitraitcollection/subscript%28_%29-9nfd8.md)
### Type Methods
- [+ traitCollectionWithCGFloatValue:forTrait:](./uitraitcollection/traitcollectionwithcgfloatvalue_fortrait_.md)
- [+ traitCollectionWithNSIntegerValue:forTrait:](./uitraitcollection/traitcollectionwithnsintegervalue_fortrait_.md)
- [+ traitCollectionWithObject:forTrait:](./uitraitcollection/traitcollectionwithobject_fortrait_.md)
- [+ traitCollectionWithResolvesNaturalAlignmentWithBaseWritingDirection:](./uitraitcollection/traitcollectionwithresolvesnaturalalignmentwithbasewritingdirection_.md)
- [+ traitCollectionWithSystemPrefersReducedResourceUsage:](./uitraitcollection/traitcollectionwithsystemprefersreducedresourceusage_.md)
- [+ traitCollectionWithTypesettingLanguage:](./uitraitcollection/traitcollectionwithtypesettinglanguage_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adaptivity
- [protocol UITraitEnvironment](./uitraitenvironment.md)
  A set of methods that makes the iOS interface environment available to your app.
- [Automatic trait tracking](./automatic-trait-tracking.md)
  Reduce the need to manually register for trait changes when you use traits within a method or closure that supports automatic trait tracking.
- [protocol UIAdaptivePresentationControllerDelegate](./uiadaptivepresentationcontrollerdelegate.md)
  A set of methods that, in conjunction with a presentation controller, determine how to respond to trait changes in your app.
- [protocol UIContentContainer](./uicontentcontainer.md)
  A set of methods for adapting the contents of your view controllers to size and trait changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uitraitcollection)*