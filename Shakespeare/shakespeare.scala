// Import necessary modules
import scala.io.Source
import scala.io.StdIn._
import java.io._

// Create an object
object WordCount {

  def main (args: Array[String]): Unit = {

    val filename = "/home/asad/Documents/Techfield/shakespeare.txt"
    val allwords = Source.fromFile(filename).mkString.toLowerCase().replaceAll("""([\p{Punct}])""", "").split("\\s+")

    val wordCounter = scala.collection.mutable.HashMap[String, Int]()
    for (word <- allwords) {
      val count = wordCounter.getOrElse(word, 0)
      wordCounter(word) = count + 1
    }

    // Make array of strings from map using string interpolation
    val str = for ( (k,v) <- wordCounter) yield s"$k,$v"

    // Create file writer
    val pw = new java.io.PrintWriter(new File("WordCount.csv"))

    // Write each map entry in new line and close
    try pw.write(str.mkString("\n")) finally pw.close()

//    def main (args: Array[String]): Unit = {
      //
//    }
  }
}