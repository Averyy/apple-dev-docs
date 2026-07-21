# Defining the metadata of your Wallet Pass

**Framework**: Wallet Passes

Provide customizable information for your Wallet Pass.

#### Overview

When designing your Wallet Pass, consider what information is most important to include on the type of pass you’re creating. By defining the metadata of your Wallet Pass, you can optimize the user experience, ensuring that the pass displays all the most helpful information to people. You can even extend the pass experience beyond just the Wallet app, for example, by adding featured actions related to your pass.

With metadata, you can:

- Use semantic tags or pass fields to define what information appears on your pass.
- Use back fields and custom values to include additional information along with your pass. These fields are ideal for information that may not fit on the design of the pass itself, but that someone may still want to access when looking at their pass.
- Define your pass actions, which are quick actions that someone can see when looking at your pass in the Wallet app. These actions can include event guides, links to music, links to book a hotel or flight, or even a link to open a relevant location in Maps and get directions.

#### Add Semantic Tags

Passes with semantic tags dynamically lay out pass fields based on metadata that you provide, prioritizing the most important information in specific positions in the layout. Beyond the list of tags required for a pass to function, semantic passes support optional tags for features such as pass actions and the additional information tile.

When creating your semantic passes, remember to support backward compatibility by including pass fields in addition to the semantic tags, ensuring that customers on earlier versions of the OS can still view the pass on their devices.

##### Boarding Passes

Airline boarding passes in iOS 26 and later use semantic tags to display the most relevant information for customers. Semantic tags are broken up into five categories, which display on the pass depending on relevance:

- Flight details: Includes information such as flight number, departure and arrival information, boarding details, and any flight delays. The system displays the most important flight details in the header fields in the top-right corner of the pass, and the other flight details display below the passenger details.
- Passenger details: Includes passenger names, loyalty programs and priority status, and any special service requests such as service animals, wheelchairs, carry-on pets, or whether the passenger is an unaccompanied minor. The most relevant of these tags display as badges beneath the customer’s name.
- Airports: Contains information about the passenger’s departure and arrival airports, including airport codes, city names, time zones, and security codes.
- Security: Indicates whether the passenger is a member of TSA PreCheck, Global Entry, CLEAR, or other similar programs.
- Seats: Indicates the type of seat that a passenger booked and includes seat number, row number, level, section, seat type, and description of the seat.

![An illustration of a boarding pass with the various field highlighted.](https://docs-assets.developer.apple.com/published/76d88e5390205af2733c370fefad8cb9/pass-fields-layout-airline-boarding-pass-semantic%402x.png)

For a more detailed guide on boarding passes, see [`Creating an airline boarding pass using semantic tags`](creating-an-airline-boarding-pass-using-semantic-tags.md).

##### Event Tickets

Poster event tickets utilize semantic tags to automatically lay out relevant event information in your pass design. Semantic tags are only available for sports and live performance event tickets; all other events utilize nonposter event tickets with pass fields.

> **Note**: Certain semantic tags are required to display poster event tickets, and if you don’t include them, the system displays a nonposter event ticket instead. For more information, see [`Add the required semantic tags`](creating-an-airline-boarding-pass-using-semantic-tags#Add-the-required-semantic-tags.md).

For sports event tickets, there are three categories of semantic tags:

- Event details: General information about the event such as the event name, venue name, date, time, and admission level. The most relevant event details display in the top-right corner of the pass, whereas the other event details display in the bottom left.
- Match details: Specific to sports event tickets, this section of semantic passes includes information about the sports league, home team, and away team. Match details display in the top-left corner of the pass and typically show the abbreviation of the two teams playing.
- Seats: These tags include information about the seat number, level, row, section, and any other relevant details. You can also assign a section color to help people easily find their assigned seat or seating area. This color  replaces the material strip at the bottom of the pass.

![An illustration of an event pass with the various fields highlighted.](https://docs-assets.developer.apple.com/published/63e2cbbb73058b6e0af7d3d8587613c2/pass-fields-layout-poster-event-ticket-sports%402x.png)

For live performance event tickets, there are three categories of semantic tags, which differ slightly from sports event tickets:

- Event details: General information about the event such as the event name, venue name, date, time, and admission level. The most relevant event details display on the top-right corner of the pass, while the other event details display on the bottom left.
- Performance details: The name of the performer and their artist ID. For events with more than one artist, you can include multiple artists in this section. These details aren’t displayed on the pass itself, but allow someone to locate more information or find music from the artists with Pass Actions in the Wallet app.
- Seats: Information about the seat number, level, row, section, and any other relevant details. You can also assign a section color to help people easily find their assigned seat or seating area. This color replaces the material strip at the bottom of the pass.

![An illustration of a live event pass  with the various fields highlighted.](https://docs-assets.developer.apple.com/published/c4280738f511a6dc239a9798206ae0f0/pass-fields-layout-poster-event-ticket-live-music%402x.png) For details about creating a poster event ticket, see [`Creating a poster event pass using semantic tags`](creating-an-event-pass-using-semantic-tags.md).

#### Add Custom Values

In addition to the standard semantic tags, you can also provide your own custom values for a pass. Note, though, that custom fields appear last in the hierarchy of semantic tags, so all other semantic tags appear in the pass design before custom values. These values can only appear on the pass depending on the number of other semantic tags already included.

If there’s no space on the pass for your custom values, they instead appear as standalone fields when someone views the pass in the Wallet app. Viewers can click through and see the details of all your custom value fields.

#### Provide Content for Your Pass Fields

Pass fields are static areas of the pass layout where you can add information with specific attributes related to the pass content. Pass fields have different layouts depending on the pass style.

##### Boarding Passes

Airline boarding passes before iOS 26 and all other types of boarding passes use pass fields to lay out their content.

The header of the pass contains fields for a logo, logo text, and header. You can use the logo and logo text fields to identify your brand. The header field contains information such as gate number and flight details, which someone may want to view at a glance on your pass.

The primary fields display airport codes. The auxiliary and secondary fields display all other relevant information, such as dates and times of the trip, flight class, terminals, gates, boarding groups, and seat number.

> **Note**: Unlike other pass types, on boarding passes, the auxiliary fields appear above the secondary fields.

![An illustration of an airline boarding pass  with the various fields highlighted.](https://docs-assets.developer.apple.com/published/7596c8e417b71168337c5ba20bee9f6e/pass-fields-layout-airline-boarding-pass%402x.png)

For a more details on boarding passes, see [`Creating an airline boarding pass using semantic tags`](creating-an-airline-boarding-pass-using-semantic-tags.md).

##### Coupons

Setting the coupon pass style provides data that Wallet displays automatically, such as business information, offer expiration date, terms and conditions, store locations, and other helpful information. The pass’s style determines the overall visual appearance of the pass and the template for placement of information on the pass. The following illustration shows the layout and placement of fields for the coupon pass style:

![An illustration of a coupon pass with the various fields highlighted.](https://docs-assets.developer.apple.com/published/52ddae96bb78f680b7f634d2e269d1c4/pass-fields-layout-coupon%402x.png) For details on creating a coupon, see [`Creating a coupon pass`](creating-a-coupon-pass.md).

##### Event Tickets

Nonposter event tickets use pass fields for their layout content. Whereas live performances and sports event tickets may use semantic poster event tickets, other events such as movies, conferences, conventions, workshops, social gatherings, or generic events use pass fields for their layouts.

![An illustration of a nonposter event ticket with the various fields highlighted.](https://docs-assets.developer.apple.com/published/44db4b65a5f736938ca777e3530e6fba/pass-fields-layout-event-ticket%402x.png) For more information about using pass fields on nonposter event tickets, see [`Ensure backward compatibility`](creating-an-event-pass-using-semantic-tags#Ensure-backward-compatibility.md).

##### Store Cards

A store card pass can display a logo, strip images, and a barcode, and it can have up to four secondary and auxiliary fields, all displayed on one row. The text length in each pass field determines how many fields appear on the front of the pass. If the text is too long, Wallet won’t display all of it.

![An illustration of a store card pass with the various fields highlighted.](https://docs-assets.developer.apple.com/published/d961d8a2137f4feb9fcfff957450a623/pass-fields-layout-store-card%402x.png)

For details on creating a store card, see [`Creating a store card pass`](creating-a-store-card-pass.md).

##### Generic Passes

Both the generic pass and the generic poster pass use pass fields, but they have slightly different layouts for the fields.

Generic poster passes put the primary focus on the background image of the pass, which is why the layout is slightly different than the generic pass.

![An illustration of a generic pass for a museum with the various fields highlighted.](https://docs-assets.developer.apple.com/published/67f2ccba4d6fc356394ba6b995efff67/pass-fields-layout-poster-generic%402x.png)

On a generic pass, the primary fields appear larger in the top section of the pass. They don’t extend across the pass to leave room for the thumbnail image.

Generic passes also allow for up to four secondary fields and four auxiliary fields. Unlike other pass types that collapse secondary and auxiliary fields into one section, generic passes keep them separate, allowing for a total of eight displayed fields.

![An illustration of a generic pass for a gym with the various fields highlighted.](https://docs-assets.developer.apple.com/published/04a42ba466f637bc1bdf9a67deb3e15a/pass-fields-layout-generic-pass%402x.png)

For details on how to create a generic pass, see [`Creating a generic pass`](creating-a-generic-pass.md).

#### Add Any Relevant Back Fields

Back fields are available for every pass type, but they don’t appear in the layout of the pass itself. Use this field to provide additional, noncritical information. Back fields are only visible when someone views their pass in the Wallet app and selects Pass Details.

#### Add Featured Actions

You can also include featured actions with your pass. These actions display as cards when viewing your pass in the Wallet app and you can use them for quick calls to action for the viewer. Featured actions make it easy for someone to quickly find relevant information related to your pass, such as directions to a business location, music related to a live performance, or even quick links to book tickets.

![An illustration of a generic pass with two featured action options: View Membership Benefits and Go to Location.](https://docs-assets.developer.apple.com/published/b0d2cb7aa567cb9060b1816230095d97/featured-actions-with-pass%402x.png)

Each featured action includes an icon, string, and action. You define your icon from available SF Symbols; be sure to pick one that accurately represents the action and that viewers can easily understand at a glance. Also, when choosing a symbol, prefer circular, filled icons. Your string is a brief call to action and your action label informs people what happens when they click the link; for example, your pass may redirect them to a website or the Maps app. ![An image of a featured action icon with labels.](https://docs-assets.developer.apple.com/published/cf870ba4be72c85d1a2d080e9f3efd87/featured-actions-anatomy%402x.png)

Certain predefined featured actions are recommended for specific pass types, such as `View Schedule` for an event ticket or `View Membership Benefits` for a membership pass. See the full list of available featured actions below:

| Preview | Action | Purpose | API | Category |
| --- | --- | --- | --- | --- |
| ![An image of the View Schedule feature action.](https://docs-assets.developer.apple.com/published/ba822eb76a24ebfd4647ed052bb52f54/featured-actions-viewschedule%402x.png) | View Schedule | Opens link to view event schedule | `viewSchedule` | Events |
| ![An image of the Watch Trailer feature action.](https://docs-assets.developer.apple.com/published/41b53d3a547a9f3aa02d74372dd9c245/featured-actions-watchtrailer%402x.png) | Watch Trailer | Opens link to watch a trailer for an upcoming event | `watchTrailer` | Events |
| ![An image of the Listen to Music feature action.](https://docs-assets.developer.apple.com/published/a5bb3767ca6463c9fd5c76b77bdaaa6e/featured-actions-listentomusic%402x.png) | Listen to Music | Opens link to playlist to listen to musical artist(s) | `listenToMusic` | Events |
| ![An image of the call feature action.](https://docs-assets.developer.apple.com/published/9aa7b6c18d7d24bf2d504e0ff856bde4/featured-actions-call%402x.png) | Call | Opens phone app to call support call | `call` | Generic |
| ![An image of the Go to Location feature action.](https://docs-assets.developer.apple.com/published/558d6d04aca36af405ab57ca2cae7eff/featured-actions-place%402x.png) | Go to Location | Opens Maps to singular location. | `place` | Generic |
| ![An image of the call feature action.](https://docs-assets.developer.apple.com/published/9aa7b6c18d7d24bf2d504e0ff856bde4/featured-actions-call%402x.png) | Call | Opens phone app to call support | `call` | Generic |
| ![An image of the Go to Location feature action.](https://docs-assets.developer.apple.com/published/558d6d04aca36af405ab57ca2cae7eff/featured-actions-place%402x.png) | Go to Location | Opens Maps to a singular location | `place` | Generic |
| ![An image of the Add to Balance feature action.](https://docs-assets.developer.apple.com/published/d939952307894830b02063408cb5379c/featured-actions-addtobalance%402x.png) | Add to Balance | Opens link to load balance | `addToBalance` | Membership |
| ![An image of the Order Delivery or Pickup feature action.](https://docs-assets.developer.apple.com/published/5a88d05a8972c75b268e59dedaac5545/featured-actions-order%402x.png) | Order Delivery or Pickup | Opens link to facilitate pickup or delivery service | `order` | Membership |
| ![An image of the Shop Online or In-App feature action](https://docs-assets.developer.apple.com/published/4dcf119ebfef33e7b5d45b76683816d7/featured-actions-shop%402x.png) | Shop Online or In-App | Opens a link either online or in-app to e-commerce store | `shop` | Membership |
| ![An image of the Shop Online or In-App feature action](https://docs-assets.developer.apple.com/published/4dcf119ebfef33e7b5d45b76683816d7/featured-actions-shop%402x.png) | Shop Online or In-App | Opens link either online or in your app to an e-commerce store | `shop` | Membership |
| ![An image of the View Membership Benefits feature action.](https://docs-assets.developer.apple.com/published/a1478f28abda2be85fe02d961c47e171/featured-actions-membershipbenefits%402x.png) | View Membership Benefits | Opens link to view membership benefits, points, and tiers for a membership program, either in your app or on your company’s website | `membershipBenefits` | Membership |
| ![An image of the Book an Appointment feature action.](https://docs-assets.developer.apple.com/published/65eaccbbc928027cc8d83328c992a132/featured-actions-bookappointment%402x.png) | Book an Appointment | Opens the schedule to reserve a time slot for a service | `bookAppointment` | Membership |
| ![An image of the Book a Car feature action.](https://docs-assets.developer.apple.com/published/b75715710ce28e25810900cf7c80ffa2/featured-actions-bookcar%402x.png) | Book a Car | Quickly leads someone to your app or website to book a car with a car rental service | `bookCar` | Membership |
| ![An image of the Book a Flight feature action.](https://docs-assets.developer.apple.com/published/437f8b1679e6d593246f397042388cb3/featured-actions-bookflight%402x.png) | Book a Flight | Quickly leads someone your app or website to book a flight with airline service | `bookFlight` | Membership |
| ![An image of the Book a Car feature action.](https://docs-assets.developer.apple.com/published/b75715710ce28e25810900cf7c80ffa2/featured-actions-bookcar%402x.png) | Book a Car | Leads people to your app or website to book a car with a rental service | `bookCar` | Membership |
| ![An image of the Book a Flight feature action.](https://docs-assets.developer.apple.com/published/437f8b1679e6d593246f397042388cb3/featured-actions-bookflight%402x.png) | Book a Flight | Leads people to your app or website to book a flight with an airline service | `bookFlight` | Membership |
| ![An image of the Book a Stay feature action.](https://docs-assets.developer.apple.com/published/82c8ad0e3da06bae7693b1f4606349ca/featured-actions-bookstay%402x.png) | Book a Stay | Leads people to your app or website to book a hotel or hospitality-related stay | `bookStay` | Membership |
| ![An image of the View Offers and Rewards feature action.](https://docs-assets.developer.apple.com/published/1ef4f989b6eab07672c8d0c26dc2b143/featured-actions-viewofferrewards%402x.png) | View Offers and Rewards | Leads people to your app or website to take an action related to their membership offers or rewards | `viewOffersRewards` | Membership, Generic, Event |

## See Also

- [Creating a pass with Pass Designer](creating-a-pass-with-pass-designer.md)
  Construct and customize a variety of pass styles with this easy-to-use tool.
- [Creating the Source for a Pass](creating-the-source-for-a-pass.md)
  Create the directory structure and add source files and images to define a pass.
- [Building a Pass](building-a-pass.md)
  Build a distributable pass.
- [Distributing and updating a pass](distributing-and-updating-a-pass.md)
  Distribute a pass to your users or update an existing pass.
- [object Pass](pass.md)
  An object that represents a pass.
- [object PassFields](passfields.md)
  An object that represents the groups of fields that display information on the front and back of a pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/walletpasses/defining-the-metadata-of-your-wallet-pass)*