import kotlin.math.*

fun main() {
    var a=6.4;
    var b: Float =1560/720F;
    var c=a.pow(2)/(1+(b*b)); c=sqrt(c);
       
    println("\nHeight: $c" + " pulgadas\n")
	println("Height: ${ (2.54*c) }" + " centimetros\n")
	println("Width: ${ b*(2.54*c) }" + " centimetros\n")
}
