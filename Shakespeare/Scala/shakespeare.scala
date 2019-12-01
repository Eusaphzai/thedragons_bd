package com.assignment1.scala
import scala.io.Source
import scala.collection.mutable.{ListBuffer,Map}
import java.io._

object shakespeare {
  def main(args: Array[String]) {
    val filename = "/home/consultant/Documents/bigData/github/theDragons_bd/Shakespeare Assignment/Python/shakespeare.txt"
    val raw_words = Source.fromFile(filename).getLines.toList
    var word_list = ListBuffer[String]()
    for (i <- 0 to raw_words.length-1) {
      var temp_list = raw_words(i).mkString.toLowerCase.split("[ !.,?:;]+").toList
      /*println(temp_list)*/
      for (j <- 0 to temp_list.length-1) {
        word_list += temp_list(j)
      }
    }

    val dictionary = word_list.groupBy(identity).mapValues(_.size)
    //println(dictionary)
    //Make array of strings from map using string interpolation
    val str = for ( (k,v) <- dictionary) yield s"$k\t$v"
    // Create file writer
    val pw = new java.io.PrintWriter(new File("/home/consultant/Documents/bigData/github/theDragons_bd/Shakespeare Assignment/Scala/shakespeare_word_count.csv"))
    // Write each map entry in new line and close
    try pw.write(str.mkString("\n")) finally pw.close()
  }
}
