# Capstone Proposal

##### Judith Combs, Class Honeybadger

---
##### Project Overview
**Capstone** is a web based file hosting platform created with writers in mind, and designed to foster collaboration and feedback with flexible file sharing, comments, and real time communication to make recieving feedback from other users a painless and intuitive experience.
**Capstone** will make use of *django-channels, JS Vue, Axios*, and various social media API's for a connected experience. 
---
### Functionality
The heart of **capstone** is a user system that allows for users to retain ownership over their uploads while other users may freely download and edit/annotate/comment without compromising the integrity of the original.
**Users** will have access to a homepage where they will be able to:
-see their uploads
-upload new work
-create groups and add other users and files
-track interaction with their posts
-track group activity
*Additionally* **users** will be able to view other users pages in order to browse and comment on their work, and view **group** based whiteboards where users can concurrently view, discuss, and even edit work together in real time, while preserving its original state for its owner.
#
#### Data Models
#
##### User
-name
-email
-password
-posts (one to many)
-comments (one to many)
-social media links (one to many)
-groups (many to many)
#
##### Group
-users
-posts
-files
-comments
-room data
##### Comment
-user (foreign key)
-text 
-upload (edited file)
-group (foreign key)
#
##### Post
-user (foreign key)
-file
-text
-comments (many to many)
-date info
-children (edited versions)
#
---
### Schedule
With **15 class days** remaining I have mapped out a set of daily goals to reach in order to deliver a finished product in a timley manner, and have included post-course goals for further development

##### Day One: Friday, Nov 15
-research libraries and APIs
-set up development enviornment
-define models for user and post
-develop basic homepage
-implement text-only posts
##### Day Two: Monday, Nov 18
-define model for comment
-implement text comments on posts
-allow users to add/track other users
##### Day Three: Teusday, Nov 19
-implement file uploads for posts
-allow users to download post files
##### Day Four: Wednesday, Nov 20
-implement activity logs (possible new model)
##### Day Five: Thursday, Nov 21
-define model for group
-implement user groups with shared message board
#
**First Milestone: Minimum Viable Product**
By day five I expect to have functional user homepages, be able to store date, and deliver a group system that sends messages and tracks comments on group projects
#
##### Day Six: Friday, Nov 22
-add file uploads to comments
-allow multiple file uploads to group pool
-integrate *Django Channels*
##### Day Seven: Monday, Nov 25
-allow concurrent viewing of files within groupchat
-begin development of asynchronous group chat
##### Day Eight: Teusday, Nov 26
-continue developing group chat
-choose frontend framework and begin implementation
##### Day Nine: Wednesday, Nov 27
-continue developing group chat
-refine frontend styling
##### Day Ten: Thursday, Nov 28
-finalize group chat with file sharing
-finalize user homepage and group room styles
#
**Second Milestone: Real Time User Interaction and Feedback**
By day ten I expect to have a working group rooms that support file sharing and concurrent viewing on a group whiteboard, as well as asynchronous real-time chat
#
##### Day Eleven: Friday, Nov 29
-implement basic social media functionality, profile links, possible cross platform sharing
-begin development of basic editing functionality for text based files 
##### Day Twelve: Monday, Dec 2
-finalize edit functions
-allow users to save edited versions of file without altering the original
##### Day Thirteen: Teusday, Dec 3
-begin integration of edit functionality with group whiteboard view, owner only
-misc maintenance, revisit styling and frontent content
##### Day Fourteen: Wednesday, Dec 4
-attempt to pass ownership of file to other user within group whiteboard, to enable real time collaborative editing
-alternately: scrap group edit functionality
-finalize styles, templates
##### Day Fifteen: Thursday, Dec 5
-revisit this document, make changes
-final testing
-prepare for presentation
#
**Third Milestone: Real Time Collaboration and Social Media Functionality**
During my demonstration I want volunteer users to create profiles, join a group, communicate via the app and edit a live document in the whiteboard.
#
##### Further Development
Long term goals for the project include a more expansive list of supported file types, including image and video, as well as basic web word processing with the ability to export in .pdf and .rtf formats. I would also like to pursue the true real-time edit functionality I had envisioned, as opposed to the more schedule-friendly one-typist-at-a-time version. 


