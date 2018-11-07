# cli-twitter
A command line for your social network!

## Why
This program is meant to make it possible to completely run a Twitter
account without needing to user a browser. Why would we want to do this?
Because it's cool. Why else?

## Dependencies
* python2-oauth2
* A web browser (I know this is for cli, but twitter auth requires it.)
* Some variation of bash.




## TODO

### Features

##### [x] is complete, [ ] is TBD
- [x] 0. Add Account
  - [x] Auth twitter
- [ ] 1. Select Account
  - [x] Display accounts in order of creation.
  - [x] Selection via number.
  - [ ] Functioning account
    - [x] Post
      - [x] Post text.
      - [x] Post image & text.
      - [x] Handle character limits.
    - [ ] Check DMs (Is this even possible?)
      - [ ] Read DM
      - [ ] Respond to DM
      - [ ] Create DM (????)
    - [ ] Notifications (maybe display this at top left.)
    - [x] Read Time Line
      - [x] Create pagination.
    - [x] Logout
- [ ] 2. Remove Account
  - [ ] os.sys('rm account')
- [x] 3. Quit
- [ ] ???

#### Features thought of while working
- [ ] Timeline
  - [ ] Add "respond to tweet" option. 
- [ ] Account menu
  - [ ] display { Account Name , Notifications , Messages }

### Currently working on
- [ ] TBD.


## License

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.