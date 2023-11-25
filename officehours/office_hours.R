suppressMessages(library("lubridate"))
suppressMessages(library("stringr"))

who            <- ("Sean Burns, PhD, Associate Professor")
office_hours   <- ("Today my office hours are from 1-3PM!")
lamentation    <- ("Alas, I do not have office hours today.")
come_back      <- ("Come back on Tue or Thu, 1-3PM!")
correspondence <- ("Or email me at: sean.burns@example.edu")
message        <- c(lamentation, come_back, correspondence)

cat(who, fill=TRUE)

if(wday(today()) == 3 || wday(today()) == 5) {
  cat(office_hours, fill=TRUE)
} else {
  cat(str_wrap(message, width=35), fill=TRUE)
}
