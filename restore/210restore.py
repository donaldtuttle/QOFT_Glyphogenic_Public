diff --git a//dev/null b//tests/test_\317\210restore.py"
index 0000000000000000000000000000000000000000..45894d4927763c80cba5998ce83a3ea306babd59 100644
--- a//dev/null
+++ b//tests/test_\317\210restore.py"
@@ -0,0 +1,30 @@
+import sys
+from pathlib import Path
+sys.path.append(str(Path(__file__).resolve().parents[1]))
+import json
+import simulations.Ψrestore_reentry_stub as reentry
+
+
+def test_psi_restore(tmp_path):
+    dummy_state = {
+        "observer": "test_ψ",
+        "semantic_phase": 3,
+        "entropy": 0.42,
+        "final_state": {"reentry_available": True}
+    }
+
+    dummy_file = tmp_path / "test_ψreentry.json"
+    with open(dummy_file, "w", encoding="utf-8") as f:
+        json.dump(dummy_state, f)
+
+    reentry.TRACE_FILE = str(dummy_file)
+    reentry.OUTPUT_FILE = str(tmp_path / "output.json")
+
+    reentry.main()
+
+    with open(reentry.OUTPUT_FILE, "r", encoding="utf-8") as f:
+        result = json.load(f)
+
+    assert result["reentry_invoked"] is True
+    assert result["observer_id"] == "ψᴽ-001"
+    assert "glyph_path" in result
