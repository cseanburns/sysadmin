(display "C. Sean Burns, PhD")(newline)
(display "Associate Professor")(newline)
(display "sean.burns@uky.edu")(newline)
(newline)
(display "OFFICE HOURS:")(newline)

(define office-hours-table
  '(("wed" . "12-2pm")
    ("thu" . "9-11am")))

(define (office-hours)
  (display "Enter day of week (mon..fri): ")
  (let* ((day (string-downcase (get-line (current-input-port))))
         (pair (assoc day office-hours-table)))
    (cond
      (pair
        (display "Office hours are ")
        (display (cdr pair))
        (display ".")(newline)
      (else
        (display "No office hours today. Schedule an appointment!")(newline)))))
