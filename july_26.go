package main
import (
    "fmt"
)

func main() {
    // read input
    n := readInt()
    var sticks []int
    for i := 0; i < n; i++ {
        sticks = append(sticks, readInt())
    }
    
    // find the min

    for {
        if n < 1 {
            break
        }
        fmt.Println(n)
        min := sticks[0]
        for _, s := range sticks {
            if s < min {
                min = s
            }
        }
    
    // cut the sticks
        var new_sticks []int
        for _, s := range sticks {
            s -= min
            if s > 0 {
                new_sticks = append(new_sticks, s)
            } else {
                n--
            }
        }
        sticks = new_sticks 
    }
}


func readInt() int {
    var n int
    _, err := fmt.Scanf("%d", &n)
    if err != nil {
        panic(err)
    }
    return n
}