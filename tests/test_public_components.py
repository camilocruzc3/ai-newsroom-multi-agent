import unittest

from ai_newsroom.editorial_validation import validate_source_url, validate_summary
from ai_newsroom.workflow_states import Edition, EditionState


class EditorialTests(unittest.TestCase):
    def test_valid_synthetic_summary(self):
        self.assertEqual([], validate_summary("Example", "A synthetic news summary."))
    def test_missing_title(self):
        self.assertTrue(validate_summary("", "Some content."))
    def test_summary_word_limit(self):
        self.assertTrue(validate_summary("Example", "one two three", max_words=2))
    def test_valid_source_syntax(self):
        self.assertEqual([], validate_source_url("https://example.org/news"))
    def test_reject_credentials(self):
        self.assertTrue(validate_source_url("https://user:pass@example.org/item"))
    def test_reject_non_http_scheme(self):
        self.assertTrue(validate_source_url("file:///etc/passwd"))


class WorkflowTests(unittest.TestCase):
    def test_ordered_transitions(self):
        edition = Edition("synthetic-001")
        for state in (EditionState.RESEARCHED, EditionState.EDITED, EditionState.READY_FOR_REVIEW, EditionState.APPROVED, EditionState.DELIVERED):
            edition = edition.advance(state)
        self.assertEqual(EditionState.DELIVERED, edition.state)
    def test_cannot_deliver_unapproved_draft(self):
        with self.assertRaises(ValueError):
            Edition("synthetic-001").advance(EditionState.DELIVERED)
    def test_revise_after_review(self):
        edition = Edition("synthetic-001", EditionState.READY_FOR_REVIEW)
        self.assertEqual(EditionState.EDITED, edition.advance(EditionState.EDITED).state)


if __name__ == "__main__":
    unittest.main()
