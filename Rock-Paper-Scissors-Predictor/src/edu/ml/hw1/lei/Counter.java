package edu.ml.hw1.lei;

public class Counter {
	private String name;
	private int count;
	private String code;

	public static Counter getMax(Counter a, Counter b) {
		return a.getCount() > b.getCount() ? a : b;
	}

	public String getCode() {
		return code;
	}

	public void setCode(String code) {
		this.code = code;
	}

	public Counter(String name, int count, String code) {
		this.name = name;
		this.count = count;
		this.code = code;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public int getCount() {
		return count;
	}

	public void setCount(int count) {
		this.count = count;
	}
}
