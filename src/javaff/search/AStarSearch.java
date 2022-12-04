package javaff.search;

import javaff.planning.State;
import javaff.planning.Filter;
import java.util.Comparator;
import java.util.TreeSet;
import java.util.Hashtable;

public class AStarSearch extends Search {
  protected Hashtable closed;
  protected TreeSet open;
  protected Filter filter = null;

  public AStarSearch(State s) {
    this(s, new HGValueComparator());
  }

  public AStarSearch(State s, Comparator c) {
    super(s);
    setComparator(c);

    closed = new Hashtable();
    open = new TreeSet(comp);
  }

  public void setFilter(Filter f) {
    filter = f;
  }

  public void updateOpen(State S) {
    open.addAll(S.getNextStates(filter.getActions(S)));
  }

  public State removeNext() {
    State S = (State) ((TreeSet) open).first();
    open.remove(S);
    return S;
  }

  public boolean needToVisit(State s) {
    Integer Shash = Integer.valueOf(s.hashCode());
    State D = (State) closed.get(Shash);

    if (closed.containsKey(Shash) && D.equals(s))
      return false;

    closed.put(Shash, s);
    return true;
  }

  public State search() {

    open.add(start);

    while (!open.isEmpty()) {
      State s = removeNext();
      if (needToVisit(s)) {
        ++nodeCount;
        if (s.goalReached()) {
          return s;
        } else {
          updateOpen(s);
        }
      }

    }
    return null;
  }
}
