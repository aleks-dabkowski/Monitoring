import streamlit as st
import psutil
import time


st.set_page_config(
    page_title="Monitoring",
    page_icon="📊",
    layout="centered"
)

st.title("Monitoring")

memory = psutil.virtual_memory()
disk = psutil.disk_usage('/')

st.header("Systemauslastung:")
st.metric(label="CPU-Auslastung (%):", value=psutil.cpu_percent(interval=1))
st.metric("Ram-Auslastung (%):",
      round(memory.percent))
st.metric("Speichernutzung (%):",
      disk.percent)
st.metric("Unbenutzter Speicher (in GB):",
      round(disk.free /(1024**3), 2))

st.header("System Spezifikationen:")
st.subheader("CPU:")
st.metric("Logische Kerne:",
      psutil.cpu_count())
st.metric("Physische Kerne:",
      psutil.cpu_count(logical=False))
st.subheader("RAM:")
st.metric("Gesamter RAM (in GB):",
      round(memory.total / (1024**3), 2))
st.subheader("Speicher:")
st.metric("Gesamter Speicher (in GB):",
      round(disk.total / (1024**3), 2))


time.sleep(1)
st.rerun()

