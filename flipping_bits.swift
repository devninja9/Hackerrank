func flippingBits(n: Int) -> Int {
    var number = n
    var ret = 0

    for i in 1...32 {
        let bin = number % 2 > 0 ? 0 :  1
        ret = ret + bin * Int(pow(Double(2), Double(i - 1)))
        number /= 2
    }
    
    return ret
}
