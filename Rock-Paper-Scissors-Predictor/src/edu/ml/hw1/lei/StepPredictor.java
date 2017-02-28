package edu.ml.hw1.lei;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Random;

public class StepPredictor {
	private List<String> humanHistory = new ArrayList<>(100);
	private List<String> machineHistory = new ArrayList<>(100);
	private String[] humanThreeRounds = new String[] { "0", "1", "1" };
	private String[] machineThreeRounds = new String[] { "0", "1", "1" };
	private Counter result;
	private Random rd = new Random();
	private Map<String, String> map = new HashMap<>();

	public StepPredictor() {
		map.put("0", "Rock");
		map.put("1", "Paper");
		map.put("2", "Scissor");
	}

	public void startPredict() {
		System.out.println("Please input what machine has played: ");
		BufferedReader br = null;
		String line = "";

		try {
			br = new BufferedReader(new InputStreamReader(System.in));
			line = br.readLine();
			while (line != null) {
				predictNextStep();
				updateMachineThreeRounds(line);
				updateHumanThreeRounds(result.getName());
				line = br.readLine();
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			if (br != null) {
				try {
					br.close();
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		}
	}

	public void updateMachineThreeRounds(String input) {
		machineThreeRounds[0] = machineThreeRounds[1];
		machineThreeRounds[1] = machineThreeRounds[2];
		machineThreeRounds[2] = input;
	}

	public void updateHumanThreeRounds(String input) {
		humanThreeRounds[0] = humanThreeRounds[1];
		humanThreeRounds[1] = humanThreeRounds[2];
		humanThreeRounds[2] = input;

	}

	public void predictNextStep() {
		Counter rockCounter = new Counter("0", 0, "Rock");
		Counter paperCounter = new Counter("1", 0, "Paper");
		Counter scissorCounter = new Counter("2", 0, "Scissors");

		for (int i = 0; i < 96; i++) {
			if (humanThreeRounds[0].equals(humanHistory.get(i)) && humanThreeRounds[1].equals(humanHistory.get(i + 1))
					&& humanThreeRounds[2].equals(humanHistory.get(i + 2))
					&& machineThreeRounds[0].equals(machineHistory.get(i))
					&& machineThreeRounds[1].equals(machineHistory.get(i + 1))
					&& machineThreeRounds[2].equals(machineHistory.get(i + 2))) {
				if (machineHistory.get(i + 4).equals(0))
					rockCounter.setCount(rockCounter.getCount() + 1);
				else if (machineHistory.get(i + 4).equals(1))
					paperCounter.setCount(paperCounter.getCount() + 1);
				else if (machineHistory.get(i + 4).equals(1))
					scissorCounter.setCount(scissorCounter.getCount() + 1);
			}
		}
		if (rockCounter.getCount() == 0 && paperCounter.getCount() == 0 && scissorCounter.getCount() == 0) {
			int code = rd.nextInt(2);
			result = new Counter(String.valueOf(code), 0, map.get(String.valueOf(code)));
		} else {
			result = Counter.getMax(rockCounter, Counter.getMax(paperCounter, scissorCounter));
		}
		System.out.println("You should play " + result.getCode());
	}

	public void readData(String filePath) {
		BufferedReader br = null;
		String line;
		String separator = ",";

		try {
			br = new BufferedReader(new FileReader(filePath));
			while ((line = br.readLine()) != null) {
				String[] tmp = line.split(separator);
				humanHistory.add(tmp[0]);
				machineHistory.add(tmp[1]);
			}
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			if (br != null) {
				try {
					br.close();
				} catch (IOException e) {
					e.printStackTrace();
				}
			}
		}
	}
}
