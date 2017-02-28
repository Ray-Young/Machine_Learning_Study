package edu.ml.hw1.lei;

public class Main {
	public static void main(String[] args) {
		StepPredictor s = new StepPredictor();
		s.readData("source_data.csv");
		while (true) {
			s.startPredict();
		}
	}
}
