graph [
  node [
    id 0
    label 1
    disk 3
    cpu 1
    memory 1
  ]
  node [
    id 1
    label 2
    disk 1
    cpu 2
    memory 1
  ]
  node [
    id 2
    label 3
    disk 7
    cpu 2
    memory 12
  ]
  node [
    id 3
    label 4
    disk 6
    cpu 2
    memory 11
  ]
  node [
    id 4
    label 5
    disk 5
    cpu 4
    memory 13
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 198
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 82
  ]
  edge [
    source 0
    target 2
    delay 29
    bw 105
  ]
  edge [
    source 1
    target 4
    delay 26
    bw 192
  ]
  edge [
    source 2
    target 3
    delay 26
    bw 135
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 81
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 99
  ]
]