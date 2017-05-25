package com.sreejithpillai.hbase.bulkload;

public enum HColumnEnum {
	  COL_ARTIST ("artist".getBytes()),
	  COL_GENRE ("genre".getBytes()),
	  COL_STYLE ("style".getBytes()),
	  COL_COUNTRY ("country".getBytes()),
	  COL_RELEASED ("released".getBytes()),
	  COL_NOTES ("notes".getBytes());
	 
	  private final byte[] columnName;
	  
	  HColumnEnum (byte[] column) {
	    this.columnName = column;
	  }

	  public byte[] getColumnName() {
	    return this.columnName;
	  }
	}