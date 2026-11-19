# MyWB Privacy Policy

Effective date: November 18, 2026

MyWB is a local desktop application for research use. It is designed to run
on your computer and process files that you choose to open, create, or save.

## Data Collection

MyWB does not require a user account in its account-free releases and does not
ask for your name, email address, postal address, or payment information.

MyWB does not transmit your research data, file contents, images, settings,
labels, or measurements to the developer or an online service.

If you switch on AI Assistant Access, MyWB provides the information described
under AI Assistant Access below to the assistant program you connect on the
same computer. MyWB does not send that information to the developer or to a
MyWB service. Whether the assistant transmits it onward is decided by that
program and not by MyWB.

MyWB does not include individual behavioral analytics, advertising identifiers,
persistent remote tracking, or automatic crash reporting.

Limited technical request data and de-identified aggregate service totals may
be processed when MyWB performs the online checks described below. This data
is not used for advertising or behavioral profiling.

## Local Files and Research Data

Images, MyWB files, SVG exports, settings, labels, measurements, and other
user-created data remain on your computer unless you choose to share them.

MyWB may read files that you open and may write files that you save or export.
When you use PowerPoint-to-MyWB import, SVG data is read either from the local
clipboard by `Paste MyWB from PowerPoint` or from a `.pptx` file you open
(with `Open MyWB File`, by dropping it on MyWB, or in the MyWB Files panel).
The PowerPoint file, its file name and path, and the SVG data read from it are
processed locally and are not
transmitted as part of license verification. Band detection likewise analyses
the image on your computer; the image and the document are not transmitted.

Every MyWB file (`.gel.svg`) you save, and every figure you copy with
`Copy SVG for PowerPoint`, carries the document inside it, so that MyWB, or any
program that reads GelSVG, can open and check it again later. Besides the
figure itself, that can include:

- the pixels of the source images, at their full resolution;
- each source image's file name (without its folder) and a SHA-256 hash of the
  original file;
- the metadata the original image file carried, kept as it was: for example
  instrument and acquisition settings, dates and times, comments, and any
  location (GPS) or author fields;
- the region of interest, labels, band table, figure settings and the
  document's note; and
- quantification results, while `Save Results with the Document` is on.

Anyone who receives the file, a PowerPoint file the figure was pasted into, or
a copy of the figure can read all of this. MyWB itself does not send it
anywhere.

## Local Diagnostic Logs

MyWB writes diagnostic logs to a `logs` folder inside its application data
folder on your computer. These record what MyWB was doing, including requests
made through AI Assistant Access and the file paths involved, and a technical
traceback if MyWB stops unexpectedly. They are kept so that a problem can be
investigated after the fact.

These logs stay on your computer. MyWB does not transmit them to the developer
or to any service; they are sent only if you choose to attach them yourself
when contacting support. Older entries are discarded automatically as new ones
are written, so the logs do not grow without limit.

## Local Settings

MyWB may store application settings locally on your computer, such as user
preferences and recently used file or folder locations. These settings are
stored using the operating system's standard application settings storage and
are not transmitted to the developer.

## Network Access

MyWB does not require a continuous internet connection for local file
processing. Update checks and license or service status checks require an
occasional internet connection.

### Update Checks

When MyWB starts, or when you select Check for Updates, it may make an HTTPS
GET request to a MyBioApps-operated update service delivered through
Cloudflare. This request retrieves the version number of the latest stable
MyWB release. MyWB identifies its application name and version in the
User-Agent header.

The update-check request has no request body and does not include:

- a Cookie or Authorization header;
- an account, device, or installation identifier;
- a hardware fingerprint; or
- your files, file contents, file names, file paths, images, research data,
  settings, labels, annotations, or measurements.

Cloudflare processes the standard technical request information described
below when delivering the update service. The update service reads release
information bundled into its deployed configuration. It does not contact
GitHub while answering an update-check request and does not forward the
application's incoming User-Agent, Cookie, Authorization header, or other
application-supplied request headers to another service.

If MyWB reports that an update is available, choosing its release-page action
opens a fixed public GitHub repository address in your default browser. When
you visit that repository, GitHub receives the standard technical information
associated with your browser's direct connection. A latest-download link may
first contact the MyBioApps update service and then temporarily redirect your
browser to the versioned DMG asset hosted by GitHub. GitHub receives a direct
request from your browser when that redirect is followed.

MyWB does not automatically download or install updates unless this
functionality is explicitly added in a future release.

### License and Service Status Checks

MyWB may contact a MyWB-operated licensing service on first activation and
periodically afterward, including when a locally cached authorization is due
for renewal, near expiry, or expired. The check may also retrieve service
notices, including advance notice of licensing changes.

Quantification, PowerPoint-to-MyWB import (`Paste MyWB from PowerPoint` and
opening the MyWB figures in a `.pptx` file), band detection, and AI Assistant Access
require a successful online verification before first use of a Premium Feature
and at least once every 30 days afterward to remain continuously available. A
successful check permits offline use of the Premium Features for up to 30
days. That period may be shorter if a
previously announced change to access takes effect sooner. If the cached
authorization expires before verification succeeds, the Premium Features
remain unavailable until a new authorization is obtained.

The licensing design uses locally cached authorization. It is not intended to
contact the service on every application launch.

The current account-free check is an HTTPS GET request with no request body.
MyWB identifies its application name and version in the User-Agent header.

Each request includes a temporary nonce generated from 32 random bytes. The
nonce is used only to bind the signed response to that request and verify the
service time.

MyWB retains the request nonce only while checking that response. Its signed
copy may remain inside the cached authorization. It is not reused as, or
converted into, a persistent identifier.

The account-free request does not include:

- a Cookie or Authorization header;
- the cached entitlement;
- an account, device, or installation identifier;
- an operating-system value; or
- a hardware fingerprint.

The account-free licensing design does not send your name, email address,
research data, file names, file paths, or a persistent hardware fingerprint.

The signed authorization returned by the service is stored locally and is not
sent back during later account-free checks.

If a future release introduces user registration, payment processing, an
account token, or a persistent installation identifier, this policy will be
updated before that information is collected.

### Technical Request Data and Request Counts

When MyWB connects to an online service, the service provider necessarily
processes standard technical information associated with the connection. This
may include:

- the IP address;
- the request date and time;
- the requested endpoint;
- HTTP headers such as the User-Agent;
- the response status; and
- network or approximate location information inferred by the provider.

The developer may be able to see aggregate request counts and short-lived
operational logs.

The developer may use de-identified aggregate update- and license-service
request totals to understand overall service activity and app-version
adoption. These totals are not used to identify or link users, devices,
installations, or activity across different days.

If an update or license check is made near application startup, those counts
may provide an approximate indication of check frequency. They are not an
exact count of application launches or days of use because checks may be
cached or skipped, requests may be retried, and some use may occur offline.

MyWB does not send a separate per-launch or daily-activity analytics event.

The update and licensing services may use Cloudflare for hosting, security,
and delivery.

Developer-accessible Cloudflare Workers logs, when enabled for security,
reliability, troubleshooting, or creation of the de-identified aggregate totals
described above, will be retained for no longer than 7 days. If temporarily
exported for these purposes, any developer-held raw copy will be deleted within
the same period.

Raw logs will not be exported to advertising or behavioral analytics services.

Aggregated operational totals that no longer relate to an IP address, request
nonce, authorization token, or individual request may be retained longer for
capacity planning, abuse prevention, and understanding overall service activity
and app-version adoption.

Cloudflare's own processing is governed by its privacy policy.

## AI Assistant Access

MyWB can let an AI assistant running on the same computer read and change the
document you have open. This is a Premium Feature, it is off by default, and
it is switched on for one MyWB window at a time.

While it is on, MyWB runs a local server that accepts connections on
`127.0.0.1` only, on a port chosen by the operating system at startup. Every
request must carry an access token generated fresh each time MyWB starts. MyWB
publishes that address and token in a file inside your own user profile rather
than in a shared location. Any program running under your account that can
read that file can use the connection, so switch the setting off when you are
not using an assistant.

MyWB does not send any of the following to the developer or to a MyWB service.
It provides them to the assistant program you connected, on your computer, in
answer to that program's requests:

- the open document and the other documents the window holds, including the
  region of interest, marker and sample labels, the band table, per-image
  adjustments, figure style, output settings, the document's note, and
  quantification results;
- the names and paths of the document and image files the window has open,
  and of the files listed under `File > Open Recent`;
- MyWB's own application settings;
- a rendered picture of the MyWB window, one image pane, the SVG preview, the
  quantification view, or the assembly view, when the assistant asks for one;
- measurements taken from the pixels of an image pane, being intensity
  profiles of a region and the positions of the lanes, bands and membranes
  found in them, when the assistant asks for them;
- when the assistant names a folder, the names and paths of the image files,
  subfolders and MyWB files in it, what each of those image files records
  about how it was taken (such as the instrument, exposure time and date),
  and reduced pictures of the images, including images the window has not
  opened;
- when the assistant compares exposures, the number of pixels at the end of
  the scale within a region of the image files it names, and a picture of
  that region in each;
- what band detection finds in the images when the assistant runs it, being
  the positions, sizes and scores of the bands and ladder marks it found and
  the lanes and regions of interest it would place; and
- the text you write in `Settings > Integration > Assistant Notes`, which is
  provided to an assistant when it connects.

MyWB itself sends none of this off your computer. However, the assistant may
send it on to its provider's servers, as Claude and ChatGPT do, under that
provider's own terms and privacy policy. What the assistant does with that
information is governed by that assistant and not by MyWB. MyWB cannot see or
control that onward transmission, and switching this setting on is the
decision that permits it. If your images,
labels, or measurements are unpublished, confidential, or subject to
obligations owed to somebody else, decide whether an assistant may receive
them before switching access on.

Locally, MyWB stores whether access was last switched on, your Assistant Notes
presets, a record that an assistant has connected at least once (used only to
stop repeating the setup notice), a letter identifying each window with access
on, and a small launcher that lets a client find whichever MyWB is running.
None of this is transmitted to the developer. Permissions you grant an
assistant while it is working are not written to disk at all.

Switching access off closes the server immediately, as does closing the window
or Premium Access ceasing to be verified.

## User-Initiated Communication

If you contact the developer for support, you may choose to send screenshots,
files, crash details, or other information. Any such information is provided
by you voluntarily and is used only to respond to your request.

## Third-Party Components

An AI assistant you connect through AI Assistant Access is not a component of
MyWB and is not distributed with it. Its handling of the information described
above is governed by its own terms and privacy policy.

MyWB includes third-party software components. Their license terms are
described in the third-party notices and license materials included with MyWB.
Online update and licensing requests may be processed by Cloudflare. The
update service does not contact GitHub while answering an update-check request.
GitHub processes direct requests when you visit the public repository or follow
a download redirect. Those providers' handling of information is governed by
their own privacy policies.

When MyWB cannot open a GelSVG file, its message offers `Open GelSVG Viewer`,
which opens https://gelsvg.github.io/ in your web browser. MyWB does not send
the file there. The viewer reads a file you give it inside your browser and
does not upload it. The page is hosted on GitHub Pages and loads its
components from jsDelivr and PyPI, which receive the standard technical
information of your browser's requests under their own privacy policies.

## Changes

This privacy policy may be updated for future releases of MyWB. The version
included with your copy of MyWB applies to that distribution.
